from django.contrib import admin

# Register your models here.
from .models import bus,bus_stop,driver,rutes
admin.site.register(bus)
admin.site.register(bus_stop)
admin.site.register(driver)
admin.site.register(rutes)