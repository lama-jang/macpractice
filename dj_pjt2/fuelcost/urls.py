from django.urls import path
from . import views


app_name = 'fuelcost'
urlpatterns = [
    path('', views.TravelerListView.as_view(), name='home'),
    # path('<int:pk>/', views.TravelerDetailVeiw.as_view(), name='calfuel'),
    path('<int:name_id>/', views.traveler_detail, name='calfuel'),
]