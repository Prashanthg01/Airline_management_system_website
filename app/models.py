from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you need
    pass

class Airline(models.Model):
    airline_id = models.CharField(max_length=10)
    airline_name = models.CharField(max_length=100)
    departure_destination = models.CharField(max_length=100)
    departure = models.DateTimeField()
    arrival_destination = models.CharField(max_length=100)
    arrival = models.DateTimeField()
    duration = models.FloatField()
    total_seats = models.PositiveIntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.airline_id

class Passenger(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    passenger_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    luggage_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name
