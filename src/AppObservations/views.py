from django.shortcuts import render
from .models import WeatherVar, TempVar, WindVar, SolarVar
from .forms import WeatherForm, TempForm, WindForm, SolarForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'appobs/home.html',{})

# Create your views here.
def acerca(request):
    return render(request,'appobs/acerca.html',{})

@login_required
def buscar(request):
    query = request.GET.get('q', '')
    if query:
        data = TempVar.objects.filter(location__icontains=query)
    else:
        data = TempVar.objects.all()
    return render(request, "appobs/buscar_temperatura.html", {"query":query, "data":data})

@login_required
def buscarsolar(request):
    query = request.GET.get('q', '')
    if query:
        data = SolarVar.objects.filter(location__icontains=query)
    else:
        data = SolarVar.objects.all()
    return render(request, "appobs/buscar_solar.html", {"query":query, "data":data})

@login_required
def buscarwind(request):
    query = request.GET.get('q', '')
    if query:
        data = WindVar.objects.filter(location__icontains=query)
    else:
        data = WindVar.objects.all()
    return render(request, "appobs/buscar_wind.html", {"query":query, "data":data})

class TempCreateView(LoginRequiredMixin,CreateView):
    model = TempVar
    fields = ['latitude','length','date','location','value']
    template_name = "appobs/crear_temperatura.html"
    success_url = reverse_lazy('List')

class SolarCreateView(LoginRequiredMixin,CreateView):
    model = SolarVar
    fields = ['latitude','length','date','location','value']
    template_name = "appobs/crear_solar.html"
    success_url = reverse_lazy('SolarList')

class WindCreateView(LoginRequiredMixin,CreateView):
    model = WindVar
    fields = ['latitude','length','date','location','value']
    template_name = "appobs/crear_wind.html"
    success_url = reverse_lazy('WindList')

class TempDeleteView(LoginRequiredMixin,DeleteView):
    model = TempVar
    template_name = "appobs/eliminar_temperatura.html"
    success_url = reverse_lazy('List')

class SolarDeleteView(LoginRequiredMixin,DeleteView):
    model = SolarVar
    template_name = "appobs/eliminar_solar.html"
    success_url = reverse_lazy('SolarList')

class WindDeleteView(LoginRequiredMixin,DeleteView):
    model = WindVar
    template_name = "appobs/eliminar_wind.html"
    success_url = reverse_lazy('WindList')

class TempDetailView(LoginRequiredMixin,DetailView):
    model = TempVar
    template_name = "appobs/detalle_temperatura.html"
    #context_object_name = 'location'

class SolarDetailView(LoginRequiredMixin,DetailView):
    model = SolarVar
    template_name = "appobs/detalle_solar.html"
    #context_object_name = 'location'

class WindDetailView(LoginRequiredMixin,DetailView):
    model = WindVar
    template_name = "appobs/detalle_wind.html"
    #context_object_name = 'location'

class TempUpdateView(LoginRequiredMixin,UpdateView):
    model = TempVar
    fields = ['latitude','length','date','location','value']
    template_name = "appobs/actualizar_temperatura.html"
    success_url = reverse_lazy('List')

class SolarUpdateView(LoginRequiredMixin,UpdateView):
    model = SolarVar
    fields = ['latitude','length','date','location','value']
    template_name = "appobs/actualizar_solar.html"
    success_url = reverse_lazy('SolarList')

class WindUpdateView(LoginRequiredMixin,UpdateView):
    model = WindVar
    fields = ['latitude','length','date','location','value']
    template_name = "appobs/actualizar_wind.html"
    success_url = reverse_lazy('WindList')

class TempListView(LoginRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = TempVar  # Modelo con el que trabaja esta vista
    template_name = "appobs/temperatura_list.html"  # Plantilla para renderizar la lista

class SolarListView(LoginRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = SolarVar  # Modelo con el que trabaja esta vista
    template_name = "appobs/solar_list.html"  # Plantilla para renderizar la lista

class WindListView(LoginRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = WindVar  # Modelo con el que trabaja esta vista
    template_name = "appobs/wind_list.html"  # Plantilla para renderizar la lista