from django.urls import path
from cuentas.views import login, registro, user_logout
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', user_logout, name='logout'),
    ]