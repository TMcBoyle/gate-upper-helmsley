from django.contrib import admin
from . import models

class DocumentAdmin(admin.ModelAdmin):
    fields = ('description', 'documenttype', 'file', 'hide')
    list_display = ('description', 'documenttype', 'uploaded', 'file', 'hide')
    list_filter = ('documenttype',)

class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'when', 'hide')

class PersonAdmin(admin.ModelAdmin):
    list_filter = ('contact', 'councillor')
    list_display = (
        'name', 'position', 'email', 'telephone', 'contact', 'councillor', 'hide'
    )

# Register your models here.
admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.DocumentType, DocumentTypeAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Person, PersonAdmin)
