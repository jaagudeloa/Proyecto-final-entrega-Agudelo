from django.contrib import admin
from django.urls import path
from .views import home
from .views import buscar,create_temp,create_wind,create_solar,base

urlpatterns = [
    path('home/',home,name='home'),
    path('buscar_temperatura/', buscar,name='buscar_temperatura'),
    path('create_temperature/', create_temp,name="temperature"),
    path('create_wind/', create_wind,name="wind"),
    path('create_solar/', create_solar,name="solar"),
    ]