# Generated by Django 5.0.6 on 2024-06-02 13:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_weatherdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='temperature_120m',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='temperature_5m',
        ),
        migrations.RemoveField(
            model_name='weatherdata',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='temperature_2m',
            field=models.JSONField(default=dict),
        ),
    ]