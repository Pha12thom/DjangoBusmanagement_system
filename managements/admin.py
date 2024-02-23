from django.contrib import admin
from .models import Bus, Route, Schedule, Ticket, Payment, UserProfile, Testing

class BusDetails(admin.ModelAdmin):
    def details():
        bus_display = {"name", "no_plate", "departure_city", "departure_time", "seats"}
        return bus_display
    
admin.site.register(Testing)
admin.site.register(Bus, BusDetails)
admin.site.register(Route)
admin.site.register(Schedule)
admin.site.register(Ticket)
admin.site.register(Payment)
admin.site.register(UserProfile)

