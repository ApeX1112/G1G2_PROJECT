# Generated by Django 5.0.6 on 2024-06-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_weatherdata_snow_depth_weatherdata_snowfall_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdata',
            name='highlighted',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='preds_1',
            field=models.JSONField(default=dict),
        ),
    ]
