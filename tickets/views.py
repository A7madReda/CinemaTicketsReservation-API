from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservition
from rest_framework.decorators import api_view
from .serializers import GuestSerializer, MovieSerializer, ReservitionSeriliazer
from rest_framework import status, filters
from rest_framework.response import Response
# Create your views here.

# 1. without REST and no model query FBV -------> FUNCTION BASED VIEW"

def no_rest_no_model(request):
    guests = [
        {
            'id':1,
            'name':'omar',
            'mobile':1021243072,
            },
        {
            'id':2,
            'name':'ali',
            'mobile':124567895,
        }
    ]
    
    return JsonResponse (guests, safe=False)


# 2. no rest but from model 
# model data defult django without rest 

def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests':list(data.values('name','phone'))
    }
    return JsonResponse(response)


# 3. Function based views
# 3.1 GET POST 
@api_view(['GET', 'POST']) # this is a decorator for function view
def FBV_List(request):
    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    
    # POST 
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
