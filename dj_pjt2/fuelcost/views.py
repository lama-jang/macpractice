from django.shortcuts import render, get_object_or_404
from .models import FuelInfo
from django.template import loader
from django.views import generic

class TravelerListView(generic.ListView):
    model = FuelInfo
    template_name = "fuelcost/home.html"
    context_obejct_name = "traveler_list"

# class TravelerDetailVeiw(generic.DetailView):
#     model = FuelInfo
#     template_name = "fuelcost/calfuel.html"
#     context_object_name = "traveler_detail"

def traveler_detail(request, name_id):
    traveler = get_object_or_404(FuelInfo, pk=name_id)
    return render(request, 'fuelcost/calfuel.html', {'traveler': traveler})