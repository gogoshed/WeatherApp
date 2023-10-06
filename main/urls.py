from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_form, name='weather_form'),
    path('get_weather/', views.get_weather, name='get_weather'),
]