from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import GuideForm, SignUpForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from django.contrib.auth.models import User
from .models import Guide, OTPStorage
from django.core.mail import send_mail
import random
from django.shortcuts import render,redirect
from .models import Destination, Package,Review
from .models import ContactMessage  # Import the model
from django.core.mail import send_mail

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Use the new form with CAPTCHA
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/home/')
        else:
            messages.error(request, "Invalid credentials or CAPTCHA, please try again.")
    else:
        form = LoginForm()  # Use the new form with CAPTCHA

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def forget_password_view(request):
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                otp = str(random.randint(100000, 999999))
                OTPStorage.objects.update_or_create(user=user, defaults={'otp': otp})
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}',
                    'admin@example.com',
                    [email],
                    fail_silently=False,
                )
                request.session['reset_email'] = email
                return redirect('reset_password')
            except User.DoesNotExist:
                form.add_error('email', 'Email not found.')
    else:
        form = ForgetPasswordForm()
    return render(request, 'forget_password.html', {'form': form})

def reset_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            new_password = form.cleaned_data['new_password']
            email = request.session.get('reset_email')
            if email:
                try:
                    user = User.objects.get(email=email)
                    otp_obj = OTPStorage.objects.get(user=user)
                    if otp_obj.otp == otp:
                        user.set_password(new_password)
                        user.save()
                        otp_obj.delete()
                        return redirect('login')
                    else:
                        form.add_error('otp', 'Invalid OTP')
                except (User.DoesNotExist, OTPStorage.DoesNotExist):
                    form.add_error('otp', 'Invalid attempt')
            else:
                form.add_error(None, 'Session expired, try again')
    else:
        form = ResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form})
@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('/')




def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        # Save message to database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Send confirmation email (optional)
        send_mail(
            "New Contact Message",
            f"Name: {name}\nEmail: {email}\nMessage: {message}",
            "your-email@example.com",  # Replace with your email
            ["admin@example.com"],  # Replace with the admin email
            fail_silently=False,
        )

        return redirect("contact")  # Redirect to the same page

    return render(request, "contact.html")

def home(request):
    return render(request, 'home.html')

def packages(request):
    all_packages = Package.objects.all()
    return render(request, 'packages.html', {'packages': all_packages})

def destination(request):
    destination = Destination.objects.all()
    print(destination)  # Debugging line to check data
    return render(request, 'destination.html', {'destination': destination})

def reviews(request):
    reviews_list = Review.objects.all().order_by('-date')  # Fetch all reviews
    return render(request, 'reviews.html', {'reviews': reviews_list})

def guide_list(request):
    guides = Guide.objects.all()
    return render(request, 'guide_list.html', {'guides': guides})

def add_guide(request):
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guide_list')
    else:
        form = GuideForm()
    return render(request, 'add_guide.html', {'form': form})