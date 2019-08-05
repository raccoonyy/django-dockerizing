import requests

from django.conf import settings
from django.http import JsonResponse


def message(request):
    api_url = f'http://{settings.API_HOST}/api/'
    response = requests.get(api_url)
    return JsonResponse({'message': response.json().get('API_HOST')})


def database(request):
    database_url = settings.DATABASES['default']
    return JsonResponse({'database': database_url})


def api(request):
    return JsonResponse({'API_HOST': f'{settings.API_HOST}'})
