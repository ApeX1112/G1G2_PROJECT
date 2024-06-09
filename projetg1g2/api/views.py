from django.shortcuts import render
from django.http import JsonResponse
from .models import airport , WeatherData
from .serializers import AirportSerializer , WeatherDataSerializer
from django.db.models import Q

from modele_degivrage_test import alg1,alg2,alg3
from itertools import chain



def home(request):


    context={}
    return   render(request,'Home.html',context=context)


def LivePred(request):



    return render(request,'Live_Predictions.html')



def Dashboard(request):


    return render( request,'Dashboard.html')


def Model_inputs(request):
    q=request.GET.get('q')
    temp_data=[]
    
    if q:
        airports = airport.objects.filter(Q(name__icontains=q) | Q(country__icontains=q) | Q(city__icontains=q))
    else:
        airports=airport.objects.none()

    for airport_obj in airports :
        weather=WeatherData.objects.get(airport=airport_obj)
        snowfall_data=weather.snowfall
        snow_depth_data=weather.snow_depth
        wind_speed_10m_data=weather.wind_speed_10m
        temperature_data=weather.temperature_2m
        predictions=[]

        temperature_flat = list(chain.from_iterable(temperature_data.values()))
        wind_speed_flat = list(chain.from_iterable(wind_speed_10m_data.values()))
        snow_depth_flat = list(chain.from_iterable(snow_depth_data.values()))
        snowfall_flat = list(chain.from_iterable(snowfall_data.values()))

        for a, b, c, d in zip(temperature_flat, wind_speed_flat, snow_depth_flat, snowfall_flat):
            prediction = alg1.alg1(a, b, c, d)
            predictions.append(prediction)

        temp_data.append((airport_obj,temperature_data,snowfall_data,snow_depth_data,wind_speed_10m_data,predictions))
    
    context={ "temp_data":temp_data}
    return render( request,'Model_inputs.html',context)


def data_api(request):
    airoports_data=airport.objects.all()
    serializer = AirportSerializer(airoports_data, many=True)
    return JsonResponse(serializer.data, safe=False)



def aeroport_details(request,code):
    details=airport.objects.filter(code=code)
    serializer=AirportSerializer(details,many=True)

    return JsonResponse(serializer.data,safe=False)

def Weather_data(request,code):
    weatherdata=WeatherData.objects.get(airport__code=code)
    serializer=WeatherDataSerializer(weatherdata)

    return JsonResponse(serializer.data,safe=False)


def apis(request):

    return render(request,"API/apis.html")

def aeroports1(request):
    airoports=airport.objects.all()
    context={"airports":airoports}
    return render(request,"API/aeroport_details.html",context)


def aeroports2(request):
    airoports=airport.objects.all()
    context={"airports":airoports}
    return render(request,"API/aeroport_weather.html",context)



