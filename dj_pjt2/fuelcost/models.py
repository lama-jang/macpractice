from django.db import models

class fuel_info(models.Model):
    name = models.CharField(max_length=10)
    car = models.CharField(null=True, max_length=50)
    efficiency = models.FloatField()

    def __str__(self):
        return self.name

class trip_info(models.Model):
    traveler = models.ForeignKey(fuel_info, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.traveler
