from django.shortcuts import render
from django.http import JsonResponse
from .models import airport , WeatherData
from .serializers import AirportSerializer , WeatherDataSerializer
from django.db.models import Q



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
        temperature_data=weather.temperature_2m
        temp_data.append((airport_obj,temperature_data))
    
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



