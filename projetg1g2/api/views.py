from django.shortcuts import render
from django.http import JsonResponse
from .models import airport
from .serializers import AirportSerializer



def home(request):


    context={}
    return   render(request,'Home.html',context=context)


def LivePred(request):



    return render(request,'Live_Predictions.html')



def Dashboard(request):


    return render( request,'Dashboard.html')


def Model_inputs(request):

    
    return render( request,'Model_inputs.html')


def data_api(request):
    airoports_data=airport.objects.all()
    serializer = AirportSerializer(airoports_data, many=True)
    return JsonResponse(serializer.data, safe=False)



def aeroport_details(request,code):
    details=airport.objects.filter(code=code)
    serializer=AirportSerializer(details,many=True)

    return JsonResponse(serializer.data,safe=False)