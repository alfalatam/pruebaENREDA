# Generated by Django 3.0.6 on 2020-05-17 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='X',
        ),
    ]
