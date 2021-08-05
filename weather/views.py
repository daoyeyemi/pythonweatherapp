from django.http.response import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    return HttpResponse('Yoooooo')

def display_weather(request):
    return render(request, 'index.html')

def get_weather_info(request):
    # making text readable
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=London&appid=b55cf10b447457a324c51468a78d2076").json()
    return render(request, 'weather.html', {'response': response})