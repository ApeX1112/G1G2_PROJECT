from django.urls import path 
from .views import home , LivePred , Dashboard ,Model_inputs,data_api,aeroport_details
from .views import Weather_data , apis,aeroports1,aeroports2


urlpatterns = [
    path('',home,name='home'),
    path('LivePr',LivePred,name='LivePreds'),
    path('Dashboard',Dashboard,name='Dashboard'),
    path('Modelsinputs',Model_inputs,name='Model_inputs'),
    path('airports',data_api,name='airports'),
    path('airports/<str:code>/',aeroport_details,name='details'),
    path('airports_weather/<str:code>/',Weather_data,name='weather'),

    path('apis',apis,name='apis'),
    path('aeroports1',aeroports1,name='aeroports1'),
    path('aeroports2',aeroports2,name='aeroports2'),
    
]