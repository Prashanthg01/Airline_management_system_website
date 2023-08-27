from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView
from .forms import PassengerRegistrationForm, AirlineBookingForm
from .models import Passenger, Airline

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/custom_login.html'

####### main #######

@login_required
def home(request):
    return render(request, 'home.html')

def register_passenger(request):
    if request.method == 'POST':
        form = PassengerRegistrationForm(request.POST)
        if form.is_valid():
            passenger = form.save()
            return redirect('passenger_detail', pk=passenger.pk)  # Redirect to passenger_detail view
    else:
        form = PassengerRegistrationForm()
    return render(request, 'registration/register_passenger.html', {'form': form})

def passenger_detail(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    context = {'passenger': passenger}
    return render(request, 'registration/passenger_detail.html', context)

def book_airline(request):
    if request.method == 'POST':
        airline_id = request.POST['airline_id']
        airline_name = request.POST['airline_name']
        departure_destination = request.POST['departure_destination']
        departure = request.POST['departure']
        arrival_destination = request.POST['arrival_destination']
        arrival = request.POST['arrival']
        duration = request.POST['duration']
        total_seats = request.POST['total_seats']
        status = request.POST['status']

        # Create Airline object and save it to the database
        airline = Airline(
            airline_id=airline_id,
            airline_name=airline_name,
            departure_destination=departure_destination,
            departure=departure,
            arrival_destination=arrival_destination,
            arrival=arrival,
            duration=duration,
            total_seats=total_seats,
            status=status
        )
        airline.save()

        # Redirect to a success page or render another template
        return render(request, 'booking/book_airline_success.html')

    return render(request, 'booking/book_airline.html')

def booking_confirmation(request):
    return render(request, 'booking/booking_confirmation.html')


def passenger_detail(request):
    passenger_id = request.GET.get('passenger_id')
    if passenger_id:
        passenger = get_object_or_404(Passenger, passenger_id=passenger_id)
        return render(request, 'passenger_details.html', {'passenger': passenger})
    else:
        return render(request, 'home.html')
    
def complete_details(request):
    if 'airline_id' in request.GET:
        airline_id = request.GET['airline_id']
        airline = get_object_or_404(Airline, airline_id=airline_id)
        passengers = Passenger.objects.filter(airline=airline)

        context = {
            'airline': airline,
            'passengers': passengers,
        }
        return render(request, 'complete_details.html', context)

    return render(request, 'home.html')
