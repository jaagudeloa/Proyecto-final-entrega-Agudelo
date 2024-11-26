from django import forms

class WeatherForm(forms.Form):
    latitude = forms.DecimalField(max_digits=10, decimal_places=2,widget=forms.TextInput(attrs={'class': 'form-control'}))
    length = forms.DecimalField(max_digits=10, decimal_places=2,widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    value = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'class': 'form-control'}))

class BuscarForm(forms.Form):
    location = forms.CharField(max_length=20)

class TempForm(WeatherForm):
    pass

class WindForm(WeatherForm):
    pass

class SolarForm(WeatherForm):
    pass