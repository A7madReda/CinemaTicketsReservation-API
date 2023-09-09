from django.shortcuts import render
from django.http.request import JsonResponse

# Create your views here.

# 1. without REST and no model query FBV -------> FUNCTION BASED VIEW
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
