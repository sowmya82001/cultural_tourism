from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

from django import forms
from .models import Guide



class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField()

class ResetPasswordForm(forms.Form):
    otp = forms.CharField(max_length=6)
    new_password = forms.CharField(widget=forms.PasswordInput)

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ['name', 'phone', 'email', 'languages', 'experience', 'bio']