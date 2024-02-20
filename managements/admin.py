from django.contrib import admin
from .models import Bus, Route, Schedule, Ticket, Payment, UserProfile

admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Schedule)
admin.site.register(Ticket)
admin.site.register(Payment)
admin.site.register(UserProfile)

