from django.urls import path 
from .views import home , LivePred , Dashboard ,Model_inputs,data_api,aeroport_details


urlpatterns = [
    path('',home,name='home'),
    path('LivePr',LivePred,name='LivePreds'),
    path('Dashboard',Dashboard,name='Dashboard'),
    path('Modelsinputs',Model_inputs,name='Model_inputs'),
    path('airports',data_api,name='airports'),
    path('airports/<str:code>/',aeroport_details,name='details'),
    
]