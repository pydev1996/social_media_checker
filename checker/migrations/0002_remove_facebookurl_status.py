# Generated by Django 3.2.4 on 2023-06-30 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookurl',
            name='status',
        ),
    ]
