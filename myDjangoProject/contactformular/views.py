from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from contactformular.models import Meldeformular
# Create your views here.

def my_view(request):
    # if foo:
    #     return HttpResponseNotFound('<h1>PAGE NOT FOUND!</h1>')
    # else:
    return HttpResponse('<h1>PAGE WAS FOUND!</h1>')

def home(request):
    name = 'Every Body'
    return render_to_response('home.html', {'name': name})

def meldungen(request):
    return render_to_response('meldungen.html', {'meldungen': Meldeformular.objects.all()})

def meldung(request, person_id=1):
    return render_to_response('meldung.html', {'meldung': Meldeformular.objects.get(id=person_id)})

