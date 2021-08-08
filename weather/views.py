from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms
from .forms import CityForm
import requests

def index(request):
    return HttpResponse('Yoooooo')

def display_weather(request):
    return render(request, 'index.html')

# def get_inputvalue(request):

def get_weather_info(request):
    form = CityForm(request.POST)
    if request.method == 'POST':
            if form.is_valid():
                form.save()

    form = CityForm()
    print(request.POST.get("city_input"))
    city = request.POST.get("city_input")
    # making text readable
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid=b55cf10b447457a324c51468a78d2076".format(city)).json()
    return render(request, 'index.html', { 'response': response, 'form': form  })