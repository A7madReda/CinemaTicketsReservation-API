from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservition

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


#2. no rest but from model 
# model data defult django without rest 

def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests':list(data.values('name','phone'))
    }
    return JsonResponse(response)

