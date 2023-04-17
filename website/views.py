from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import models

# Create your views here.
def index(request: HttpRequest):
    if request.method == "GET":
        events = models.Event.objects.all()
        return render(
            request,
            'home.html',
            {
                'events': events
            }
        )
    else:
        return HttpResponseRedirect("../")

def councillors(request: HttpRequest):
    if request.method == "GET":
        councillors = models.Person.objects.filter(councillor=True)
        return render(
            request,
            'councillors.html',
            {
                'councillors': councillors
            }
        )
    else:
        return HttpResponseRedirect("../")

def documents(request: HttpRequest):
    if request.method == "GET":
        document_types = models.DocumentType.objects.all()
        documents = models.Document.objects.filter(
            documenttype__code=request.GET.get("document_type"),
            hide=False
        )
        
        return render(
            request,
            'documents.html',
            {
                'document_types': document_types,
                'documents': documents,
            }
        )
    else:
        return HttpResponseRedirect("../")

def contact(request: HttpRequest):
    if request.method == "GET":
        contacts = models.Person.objects.filter(contact=True)
        return render(
            request, 
            'contact.html', 
            {
                'contacts': contacts
            }
        )
    else:
        return HttpResponseRedirect("../")
