from rest_framework import serializers
from .models import airport , WeatherData

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = airport
        fields = ['name',
                   'lat',
                    'lon',
                    'code',
                    'country',
                    'city',
                    'state']


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=WeatherData
        fields=['temperature_2m',
                'snowfall',
                'snow_depth',
                'wind_speed_10m',
                'start',
                'end']