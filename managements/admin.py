from django.contrib import admin
from .models import Bus, Route, Schedule, Ticket, Payment, UserProfile, Testing

class BusDetails(admin.ModelAdmin):
    def details():
        bus_display = {"name", "no_plate", "departure_city", "departure_time", "seats"}
        return bus_display
    
    
class ScheduleDetails(admin.ModelAdmin):
    def detail():
        schedule = {
            "bus", "departTime", "arrivalTime","route"
        }
        return schedule
class RouteDetails(admin.ModelAdmin):
    def routed():
        routes = {
            "departure_city", "arrival_city"," distance","timeTaken", "buses"
        }  
        return routes   
    
    
admin.site.register(Testing)
admin.site.register(Bus, BusDetails)
admin.site.register(Route, RouteDetails)
admin.site.register(Schedule, ScheduleDetails)
admin.site.register(Ticket)
admin.site.register(Payment)
admin.site.register(UserProfile)

