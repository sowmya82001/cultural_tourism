from django.db import models
from django.contrib.auth.models import User


class OTPStorage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)

from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()

class Package(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    duration = models.IntegerField()  # Duration in days

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)  # Use an existing Customer ID

    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_people = models.IntegerField(default=1)


from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)  # Rating out of 5
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Guide(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    languages = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    bio = models.TextField()

    def __str__(self):
        return self.name