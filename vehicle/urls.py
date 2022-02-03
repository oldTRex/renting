from unicodedata import name
from django.urls import  include , path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
   path('', views.home , name="home"),
   
   path('vehicle', views.vehicle , name="vehicle"),

   path('rental', views.rental , name="rental"),

   path('delete/<vehicle_id>',    views.delete_vehicle,  name="delete_vehicle"),

   path('delete/<rental_id>',    views.delete_rental,  name="delete_rental"),
 
]
