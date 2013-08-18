from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from events.models import Events

# Create your views here.

def home(request):
    date = '05.05.2014'
    return render_to_response('home.html', {'date': date})
