from django.conf import settings
from django.shortcuts import render

def map_view(request):
    return render(request, 'services/map.html', {
        'api_key': settings.GOOGLE_MAPS_API_KEY
    })
