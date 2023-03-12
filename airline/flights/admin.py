# from django.contrib.admin.models import Group
from django.contrib import admin

from .models import Flight, Airport, Passenger

# admin.site.unregister(Group)


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    pass


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    pass

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    pass