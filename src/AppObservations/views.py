from django.shortcuts import render
from .models import WeatherVar, TempVar, WindVar, SolarVar
from .forms import WeatherForm, TempForm, WindForm, SolarForm
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request):
    return render(request,'appobs/home.html',{})

def base(request):
    return render(request,'appobs/base.html',{})

def weather_create(request):
    form = WeatherForm(request.POST or None)
    
    if form.is_valid():
        data = form.cleaned_data
        weather_obj = WeatherVar(latitude=data["latitude"], length=data["length"], date=data["date"], location=data["location"],value =data["value"]) 
        weather_obj.save()
        return HttpResponseRedirect('/posts/weather_list/')
    
    context = {"form":form,
               "form_type":"Create"}

    return render(request,"blog/weather_create.html",context)

def create_temp(request):
    form = TempForm(request.POST or None)
    
    if form.is_valid():
        data = form.cleaned_data
        weather_obj = TempVar(latitude=data["latitude"], length=data["length"], date=data["date"], location=data["location"],value =data["value"]) 
        weather_obj.save()
        return HttpResponseRedirect('/home/')
    
    context = {"form":form,
               "form_type":"Create"}

    return render(request,"appobs/temperature.html",context)

def create_wind(request):
    form = WindForm(request.POST or None)
    
    if form.is_valid():
        data = form.cleaned_data
        weather_obj = WindVar(latitude=data["latitude"], length=data["length"], date=data["date"], location=data["location"],value =data["value"]) 
        weather_obj.save()
        return HttpResponseRedirect('/home/')
    
    context = {"form":form,
               "form_type":"Create"}

    return render(request,"appobs/wind.html",context)


def create_solar(request):
    form = SolarForm(request.POST or None)
    
    if form.is_valid():
        data = form.cleaned_data
        weather_obj = SolarVar(latitude=data["latitude"], length=data["length"], date=data["date"], location=data["location"],value =data["value"]) 
        weather_obj.save()
        return HttpResponseRedirect('/home/')
    
    context = {"form":form,
               "form_type":"Create"}

    return render(request,"appobs/solar.html",context)

def buscar(request):
    query = request.GET.get('q', '')
    if query:
        data = TempVar.objects.filter(location__icontains=query)
    else:
        data = TempVar.objects.all()
    return render(request, "appobs/buscar_temperatura.html", {"query":query, "data":data})
