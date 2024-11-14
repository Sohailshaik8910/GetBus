from django.contrib import admin
from .models import Buses, Ticket, Passenger

# Register your models here.

class Busesadmin(admin.ModelAdmin):
    list_display = ['Bus_Name']


admin.site.register(Buses, Busesadmin)
admin.site.register(Ticket)
admin.site.register(Passenger)