from django.contrib import admin
from .models import Airline, Passenger

class PassengerAdmin(admin.ModelAdmin):
    list_display = ('name', 'airline', 'phone_number', 'email', 'age')
    list_filter = ('airline', 'gender', 'nationality')
    search_fields = ('name', 'email')

class AirlineAdmin(admin.ModelAdmin):
    list_display = ('airline_id',)

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Passenger, PassengerAdmin)
