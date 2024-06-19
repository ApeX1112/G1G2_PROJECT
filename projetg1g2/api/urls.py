from django.urls import path 
from .views import home , LivePred , Dashboard ,Model_inputs,data_api,aeroport_details
from .views import Weather_data , apis,aeroports1,aeroports2

from .views import UserCreate,HelloWorld
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



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

    path('api/register/', UserCreate.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/hello/', HelloWorld.as_view(), name='hello_world'),
    
]