from django.db import models
from django.utils import timezone

class airport(models.Model):

    lat = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=100)
    code=models.CharField(max_length=100,blank=True)
    city=models.CharField(max_length=100,blank=True)
    country=models.CharField(max_length=100,blank=True)
    state=models.CharField(max_length=100,blank=True)

    def __str__(self) -> str:
        return self.name


class WeatherData(models.Model):
    airport=models.ForeignKey(airport,on_delete=models.CASCADE)
    temperature_2m=models.JSONField(default=dict)
    snowfall=models.JSONField(default=dict)
    snow_depth=models.JSONField(default=dict)
    wind_speed_10m=models.JSONField(default=dict)
    highlighted=models.JSONField(default=dict)
    preds_1=models.JSONField(default=dict)
    start=models.DateTimeField(default=timezone.now)
    end=models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.airport.name}from :{self.start}-- to :{self.end}'