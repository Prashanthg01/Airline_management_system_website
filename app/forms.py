from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.models import CustomUser
from django import forms
from .models import Passenger, Airline

class RegistrationForm(UserCreationForm):
    # Add any additional fields you need
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class LoginForm(AuthenticationForm):
    pass

class PassengerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'

class AirlineBookingForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = '__all__'