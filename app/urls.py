from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, CustomLoginView, home
from .views import register_passenger, passenger_detail
from .views import book_airline, booking_confirmation
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('register_passenger/', register_passenger, name='register_passenger'),
    path('passenger_detail/<int:pk>/', passenger_detail, name='passenger_detail'),
    path('book_airline/', book_airline, name='book_airline'),
    path('booking_confirmation/', booking_confirmation, name='booking_confirmation'),
    path('passenger_detail/', views.passenger_detail, name='passenger_detail'),
    path('complete_details/', views.complete_details, name='complete_details'),
]
