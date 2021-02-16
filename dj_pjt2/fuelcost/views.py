from django.shortcuts import render, get_object_or_404
from .models import FuelInfo
from django.template import loader

def home(request):
    traveler_name = FuelInfo.objects.all()
    context = {'traveler_name':traveler_name}
    # traveler_name = get_object_or_404(trip_info, pk=traveler_id)

    return render(request, 'fuelcost/home.html', {'traveler_name': traveler_name})

def calfuel(request, name_id):
    selected_traveler = get_object_or_404(FuelInfo, pk=name_id)

# def cost_results(request, traveler):
