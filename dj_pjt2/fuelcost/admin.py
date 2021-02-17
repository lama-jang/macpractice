from django.contrib import admin
from .models import Traveler, FuelInfo

# admin.site.register(Traveler)
# admin.site.register(FuelInfo)

class TravelerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Traveler, TravelerAdmin)

@admin.register(FuelInfo)
class FuelInfo(admin.ModelAdmin):
    list_display = ('name', 'car', 'efficiency')


