import requests
from django.shortcuts import render
from .models import Weather
from django.contrib.auth.urls import authenticate, redirect, login, logout
from django.contrib import messages

def weather_form(request):
    return render(request, 'main/weather_form.html')

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=249b2ecbded3fdcc4cc06561754daaf5'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_description = data['weather'][0]['description']
            Weather.objects.create(city=city, temperature=temperature)
            return render(request, 'main/weather.html', {'city': city, 'temperature': temperature, 'humidity': humidity, 'weather_description': weather_description})


# def weather_details(request):
#     temperatures = [20, 22, 25, 27, 30]  # Sample temperatures over time
#     return render(request, 'main/weather_details.html', {'temperatures': temperatures})
