from rest_framework import serializers
from .models import airport , WeatherData
from django.contrib.auth.models import User

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
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user