from django.urls import path
from . import views


app_name = 'fuelcost'
urlpatterns = [
    path('', views.traveler_list, name='home'),
    # path('<int:pk>/', views.TravelerDetailVeiw.as_view(), name='calfuel'),
    path('<int:pk>/', views.traveler_detail, name='calfuel'),
]