# Generated by Django 5.1 on 2024-08-30 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_links_google_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='resume',
        ),
    ]
