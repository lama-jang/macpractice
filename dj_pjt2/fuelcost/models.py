from django.db import models


class Traveler(models.Model):
    traveler_name = models.CharField(max_length=10)

    def __str__(self):
        return self.traveler_name

class FuelInfo(models.Model):
    name = models.ForeignKey(Traveler, on_delete=models.SET_NULL, null=True)
    car = models.CharField(null=True, max_length=50)
    efficiency = models.FloatField(null=True)

    def __str__(self):
        return str(self.name)