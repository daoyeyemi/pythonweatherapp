from django.forms import ModelForm, TextInput
from weather.models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['city_name']
        widgets = { 'city_name' : TextInput(attrs={'class': 'input', 'placeholder' : 'Type city name here...', 'name' :'city_input' })}