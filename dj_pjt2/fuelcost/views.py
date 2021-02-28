from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FuelInfo
from django.template import loader
# from django.views import generic
from .forms import FuelInfoForm

# def traveler_list(request):
#     travelers = FuelInfo.objects.all()
#     context = {'travelers':travelers}
#     return render(request, 'fuelcost/home.html', context)

def traveler_list(request):
    form = FuelInfoForm()

    if request.method == 'POST':
        form = FuelInfoForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('fuelcost:calfuel'))
    errors = form.errors or None 
    return render(request, 'fuelcost/home.html', {'form': form, 'errors': errors,})


def traveler_detail(request, pk):
    traveler = get_object_or_404(FuelInfo, pk=pk)
    return render(request, 'fuelcost/calfuel.html', {'traveler': traveler})

# class TravelerListView(generic.ListView):
#     model = FuelInfo
#     template_name = "fuelcost/home.html"
#     context_obejct_name = "traveler_list"

# class TravelerDetailVeiw(generic.DetailView):
#     model = FuelInfo
#     template_name = "fuelcost/calfuel.html"
#     context_object_name = "traveler_detail"

