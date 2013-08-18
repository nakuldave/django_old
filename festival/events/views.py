from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from events.models import Events

# Create your views here.

def events(request):
    return render_to_response('events.html', {'events': Events.objects.all()})

def event(request, event_id=1):
    return render_to_response('event.html', {'event': Events.objects.get(id=event_id)})

