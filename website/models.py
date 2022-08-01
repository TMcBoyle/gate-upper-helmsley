from django.db import models

class Document(models.Model):
    """ Model representing documents.
    """
    # Fields
    document_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=256, blank=False, null=False)
    uploaded = models.DateTimeField(blank=True, null=False)
    file = models.FileField(blank=False, null=False)
    hide = models.BooleanField(blank=False, null=False, default=False)

# Create your models here.
class Event(models.Model):
    """ Model representing calendar events.
    """
    # Fields
    event_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.CharField(max_length=256, blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)
    when = models.DateTimeField(blank=False, null=False)
    hide = models.BooleanField(blank=False, null=False, default=False)

class Person(models.Model):
    """ Model representing parish councillors.
    """
    # Fields
    person_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=False, null=False)
    position = models.CharField(max_length=256, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=32, blank=True, null=True)
    contact = models.BooleanField()
    councillor = models.BooleanField()
    hide = models.BooleanField(blank=False, null=False, default=False)
