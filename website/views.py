from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render

from . import models

# Create your views here.
def index(request: HttpRequest):
    events = models.Event.objects.all()
    return render(request, 'home.dj.html', {'events': list(events.values())})

def councillors(request: HttpRequest):
    councillors = models.Person.objects.filter(councillor=True)
    return render(request, 'councillors.dj.html', {'councillors': list(councillors.values())})

def documents(request: HttpRequest):
    documents = models.Document.objects.filter(hide=False)
    return render(request, 'documents.dj.html', {'documents': list(documents.values())})

def contact(request: HttpRequest):
    contacts = models.Person.objects.filter(contact=True)
    return render(request, 'contact.dj.html', {'contacts': list(contacts.values())})
