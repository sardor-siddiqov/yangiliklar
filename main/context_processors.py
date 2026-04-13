import requests
from http.client import responses

from .models import *
from django.db.models import Count

def get_categories(request):
    categories = Category.objects.annotate(
        article_count = Count('article')
    ).order_by('-article_count')
    return {'base_categories': categories}


def get_weather(request):
    weather__data = requests.get("https://api.weatherapi.com/v1/current.json?q=fergana&lang=uzbek&key=8ec75e14526045b5825152922261204").json()
    context = {
        "temp_c": weather__data['current']['temp_c'],
        "weather_icon": weather__data['current']['condition']['icon'],
        "local_time": weather__data['location']['localtime'],
        "location": weather__data['location']['name'],
    }
    return context



