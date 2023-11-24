from django.shortcuts import render
from django.http import JsonResponse

def index(requests):
# "should access Model objects and use Templates to prepare responses."
   
    return JsonResponse({'Message': 'Hello world'})

