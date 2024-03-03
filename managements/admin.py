from django.contrib import admin
from .models import Bus, Route, Schedule, Ticket, Payment, UserProfile, Testing, Booking

class BusDetails(admin.ModelAdmin):
    def details():
        bus_display = {"name", "no_plate", "departure_city", "departure_time", "seats"}
        return bus_display
class RouteDetails(admin.ModelAdmin):
    def details():
        route_display = {"departure_city", "arrival_city", "distance", "duration"}
        return route_display
class ScheduleDetails(admin.ModelAdmin):
    def details():
        schedule_display = {"bus", "departTime", "arrivalTime", "price", "route"}
        return schedule_display
class BookingDetails(admin.ModelAdmin):
    def details():
        booking_display = {"ticket", "seat_no", "passenger_name", "passenger"}
        
        
admin.site.register(Testing)
admin.site.register(Bus, BusDetails)
admin.site.register(Route)
admin.site.register(Schedule)
admin.site.register(Ticket)
admin.site.register(Payment)
admin.site.register(UserProfile)
admin.site.register(Booking)

