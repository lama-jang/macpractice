from django.shortcuts import render
from django.http import HttpResponse
from .models import fuel_info, trip_info

def home(request):
    output = trip_info.traveler
    return HttpResponse(output)


# def cost_results(request, traveler):
