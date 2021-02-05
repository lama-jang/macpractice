from django.shortcuts import render
from django.http import HttpResponse
from .models import fuel_info, trip_info
from django.template import loader

def home(request):
    output = fuel_info.objects.all()
    if request.method == 'POST':
        selected_traveler = get_object_or_404(Fuel_info, pk=request.POST.get('traveler_id'))
        traveler.name = selected_traveler
        traveler.save()

    return render(request, 'fuelcost/home.html', {'output': output})


# def cost_results(request, traveler):
