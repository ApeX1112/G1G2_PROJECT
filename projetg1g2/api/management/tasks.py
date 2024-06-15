import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from api.models import airport

def data_upload():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Adjust to get the project root
    file_path = os.path.join(base_dir, 'test', 'airports.json')
    
    with open(file_path) as file:
        data = json.load(file)
        data = data[:50]

    for batch in data:
        lat = batch['lat']
        lon = batch['lon']
        name = batch['name']
        code = batch['code']
        city = batch['city']
        country = batch['country']
        state = batch['state']

        instance = airport(
            lat=lat,
            lon=lon,
            name=name,
            code=code,
            city=city,
            country=country,
            state=state
        )
        instance.save()

data_upload()

