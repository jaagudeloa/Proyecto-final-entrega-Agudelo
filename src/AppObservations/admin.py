from django.contrib import admin
from .models import WeatherVar, TempVar, WindVar, SolarVar

# Register your models here.
admin.site.register(WeatherVar)
admin.site.register(TempVar)
admin.site.register(WindVar)
admin.site.register(SolarVar)