from rest_framework import serializers
from .models import airport

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = airport
        fields = ['name', 'lat', 'lon','code','country','city','state']
