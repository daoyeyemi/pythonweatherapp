from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('climate/', views.display_weather, name='display_weather')
]