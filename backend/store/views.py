from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def home(request):
    data = {
        'message': "Welcome to the store"
    }

    return JsonResponse(data)
