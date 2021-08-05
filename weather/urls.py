from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('climate/', views.display_weather, name='display_weather'),
    path('city/', views.get_weather_info, name='get_weather_info')
]