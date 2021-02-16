from django.urls import path
from . import views


app_name = 'fuelcost'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:traveler_id>/', views.calfuel, name='calfuel'),
]