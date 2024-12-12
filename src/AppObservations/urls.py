from django.contrib import admin
from django.urls import path
from .views import home
from .views import buscar, buscarsolar, buscarwind
from AppObservations import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',home,name='home'),
    path('buscar_solar/', buscarsolar,name='buscar_solar'),
    path('buscar_temperatura/', buscar,name='buscar_temperatura'),
    path('buscar_wind/', buscarwind,name='buscar_wind'),
    path('temperatura/lista/', views.TempListView.as_view(), name='List'),
    path('temperatura/detalle/<int:pk>/', views.TempDetailView.as_view(), name='Detail'),
    path('temperatura/editar/<int:pk>', views.TempUpdateView.as_view(), name='Edit'),
    path('temperatura/eliminar/<int:pk>', views.TempDeleteView.as_view(), name='Delete'),
    path('temperatura/nuevo/', views.TempCreateView.as_view(), name='New'),
    path('solar/lista/', views.SolarListView.as_view(), name='SolarList'),
    path('solar/detalle/<int:pk>/', views.SolarDetailView.as_view(), name='SolarDetail'),
    path('solar/editar/<int:pk>', views.SolarUpdateView.as_view(), name='SolarEdit'),
    path('solar/eliminar/<int:pk>', views.SolarDeleteView.as_view(), name='SolarDelete'),
    path('solar/nuevo/', views.SolarCreateView.as_view(), name='SolarNew'),
    path('wind/lista/', views.WindListView.as_view(), name='WindList'),
    path('wind/detalle/<int:pk>/', views.WindDetailView.as_view(), name='WindDetail'),
    path('wind/editar/<int:pk>', views.WindUpdateView.as_view(), name='WindEdit'),
    path('wind/eliminar/<int:pk>', views.WindDeleteView.as_view(), name='WindDelete'),
    path('wind/nuevo/', views.WindCreateView.as_view(), name='WindNew'),
    path('about/',views.acerca,name="acerca")
    ]