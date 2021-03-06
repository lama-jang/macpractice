from django import forms
from .models import FuelInfo

# class FuelInfoForm(forms.Form):
#     traveler_name = forms.ModelChoiceField(queryset=FuelInfo.objects.all().order_by('name'))


class FuelInfoForm(forms.ModelForm):
    traveler_name = forms.ModelChoiceField(queryset=FuelInfo.objects.all().order_by('name'))
    class Meta:
        model = FuelInfo
