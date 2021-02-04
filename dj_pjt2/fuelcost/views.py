from django.shortcuts import render
from django.http import HttpResponse
from .models import fuel_info

def home(request):
    output = fuel_info.name
    return HttpResponse(output)

# def cost_results(request, traveler):
