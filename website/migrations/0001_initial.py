# Generated by Django 4.0.6 on 2022-08-01 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('documenttype_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=4096, null=True)),
                ('location', models.CharField(blank=True, max_length=1024, null=True)),
                ('when', models.DateTimeField()),
                ('hide', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telephone', models.CharField(blank=True, max_length=32, null=True)),
                ('contact', models.BooleanField()),
                ('councillor', models.BooleanField()),
                ('hide', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=256)),
                ('uploaded', models.DateTimeField(blank=True)),
                ('file', models.FileField(upload_to='')),
                ('hide', models.BooleanField(default=False)),
                ('documenttype', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.documenttype')),
            ],
        ),
    ]
