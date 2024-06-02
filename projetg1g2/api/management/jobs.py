import requests
import json
import pandas as pd
from ..models import WeatherData , airport
from django.utils import timezone
import openmeteo_requests
import requests_cache
from retry_requests import retry



cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)



url = "https://api.open-meteo.com/v1/forecast"

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def schedule_api():
	airoports=airport.objects.all()
	
	for airport_ins in airoports:
		lat=airport_ins.lat
		lon=airport_ins.lon

		params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,snowfall,snow_depth,wind_speed_10m"
    	}
		response = openmeteo.weather_api(url, params=params)
		
		
		hourly = response[0].Hourly()
		hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy().tolist()
		snowfall=hourly.Variables(1).ValuesAsNumpy().tolist()
		snow_depth=hourly.Variables(2).ValuesAsNumpy().tolist()
		wind_speed_10m=hourly.Variables(3).ValuesAsNumpy().tolist()


		start_time= pd.to_datetime(hourly.Time(), unit = "s")
		end_time= pd.to_datetime(hourly.TimeEnd(), unit = "s")

		chunks_temperature = chunk_list(hourly_temperature_2m, 24)
		chunks_snowfall = chunk_list(snowfall, 24)
		chunks_snow_depth = chunk_list(snow_depth, 24)
		chunks_wind = chunk_list(wind_speed_10m, 24)
		

		temperature_2m_data={f"day{i+1}": chunks_temperature[i] for i in range(7)}
		snowfall_data={f"day{i+1}": chunks_snowfall[i] for i in range(7)}
		snow_depth_data={f"day{i+1}": chunks_snow_depth[i] for i in range(7)}
		wind_data={f"day{i+1}": chunks_wind[i] for i in range(7)}
		
		weather_data , created =WeatherData.objects.get_or_create(
			airport=airport_ins,
			temperature_2m=temperature_2m_data,
			snowfall=snowfall_data,
			snow_depth=snow_depth_data,
			wind_speed_10m=wind_data,
			start=timezone.make_aware(start_time),
			end=timezone.make_aware(end_time)
		)
		
		print(f"---{airport_ins.name}'s weather data uploaded succesfully-------------")

		
	

	print('job done .................')