from django.db import models

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
    temperature_5m=models.FloatField()
    temperature_120m=models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)