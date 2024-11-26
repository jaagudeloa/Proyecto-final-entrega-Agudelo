from django.db import models
from django import forms

# Create your models here.
class WeatherVar(models.Model):
    latitude = models.DecimalField(max_digits=10,decimal_places=2)
    length = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField()
    location = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.location} {self.date} {self.value}"

class TempVar(models.Model):
    latitude = models.DecimalField(max_digits=10,decimal_places=2)
    length = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField()
    location = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.location} {self.date} {self.value}"

class WindVar(models.Model):
    latitude = models.DecimalField(max_digits=10,decimal_places=2)
    length = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField()
    location = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.location} {self.date} {self.value}"

class SolarVar(models.Model):
    latitude = models.DecimalField(max_digits=10,decimal_places=2)
    length = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField()
    location = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.location} {self.date} {self.value}"