import requests
from django.core.management.base import BaseCommand
from myapp.models import Airport, WeatherData

class Command(BaseCommand):
    help = 'Fetch current weather data for all airports'

    def handle(self, *args, **kwargs):
        airports = Airport.objects.all()
        for airport in airports:
            lat = airport.latitude
            lon = airport.longitude
            response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m')
            if response.status_code == 200:
                weather_data = response.json()
                # Assuming WeatherData is a model to store weather info
                WeatherData.objects.create(
                    airport=airport,
                    temperature=weather_data['current']['temperature'],
                    # Add other necessary fields
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully fetched weather data for {airport.name}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to fetch weather data for {airport.name}'))