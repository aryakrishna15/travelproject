# Generated by Django 4.2.6 on 2023-10-17 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_places'),
    ]

    operations = [
        migrations.DeleteModel(
            name='place',
        ),
    ]