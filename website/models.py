from django.db import models

class Document(models.Model):
    """ Model representing documents.
    """
    # Fields
    document_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=256, blank=False, null=False)
    uploaded = models.DateTimeField(blank=True, null=False, auto_now_add=True)
    file = models.FileField(blank=False, null=False)
    hide = models.BooleanField(blank=False, null=False, default=False)

    # Foreign Keys
    documenttype = models.ForeignKey(
        'DocumentType',
        on_delete=models.PROTECT,
        verbose_name="Document Type"
    )

    # String representation
    def __str__(self):
        return self.file.name

class DocumentType(models.Model):
    """ Model representing document types.
    """
    # Fields
    documenttype_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=1024, blank=False, null=False)

    # String representation
    def __str__(self):
        return self.description

# Create your models here.
class Event(models.Model):
    """ Model representing calendar events.
    """
    # Fields
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.CharField(max_length=4096, blank=True, null=True)
    location = models.CharField(max_length=1024, blank=True, null=True)
    when = models.DateTimeField(blank=False, null=False)
    hide = models.BooleanField(blank=False, null=False, default=False)
    
    # String representation
    def __str__(self):
        return self.name

class Person(models.Model):
    """ Model representing parish councillors.
    """
    # Fields
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False, null=False)
    position = models.CharField(max_length=256, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=32, blank=True, null=True)
    contact = models.BooleanField()
    councillor = models.BooleanField()
    hide = models.BooleanField(blank=False, null=False, default=False)
    
    # String representation
    def __str__(self):
        return self.name
