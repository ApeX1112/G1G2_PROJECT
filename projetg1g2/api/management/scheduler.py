from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_api, 'interval',id="fetch_weather_data", hours=6)
	
	scheduler.start()

	print("schedular started")