from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Yoooooo')

def display_weather(request):
    return render(request, 'index.html')
