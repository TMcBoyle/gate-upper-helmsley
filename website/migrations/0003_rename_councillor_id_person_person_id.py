# Generated by Django 4.0.6 on 2022-07-31 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_document_hide_event_hide_person_hide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='councillor_id',
            new_name='person_id',
        ),
    ]
