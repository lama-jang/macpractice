from django.db import models

class fuel_info(models.Model):
    name = models.CharField(max_length=10)
    car = models.CharField(null=True, max_length=50)
    efficiency = models.FloatField()

    def __str__(self):
        return self.name

class trip_info(models.Model):
    traveler = models.ForeignKey(fuel_info, on_delete=models.CASCADE, help_text='Select Your Name')
    date = models.DateField()

    class Meta:
        ordering = ['traveler']

    def __str__(self):
        return self.traveler

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
