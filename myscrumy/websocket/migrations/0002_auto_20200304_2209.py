# Generated by Django 3.0.2 on 2020-03-04 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websocket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessage',
            old_name='message',
            new_name='content',
        ),
    ]
