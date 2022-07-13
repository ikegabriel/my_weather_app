import os
from dotenv import load_dotenv
from django.shortcuts import render
import urllib.request
import json
# Create your views here.

def configure():
    load_dotenv()


def index(request):
    if request.method == 'POST':
        try:
            city = request.POST['city']
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + f'&units=metric&appid={os.getenv("weather_api_key")}').read()

            list_of_data = json.loads(source)

            data = {
                'country_code': str(list_of_data['sys']['country']),
                'coordinate': str(list_of_data['coord']['lon']) + str(list_of_data['coord']['lat']),
                'temp': str(list_of_data['main']['temp']),
                'pressure': str(list_of_data['main']['pressure']),
                'humidity': str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': str(list_of_data['weather'][0]['icon'])
            }
        except:
            data = {}
    else:
        data = {}
    return render(request, 'weather/index.html', data,)

def weather(request):
    return render(request, 'weather/api.html')