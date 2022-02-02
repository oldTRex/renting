from unicodedata import name
from django.urls import  include , path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
   path('', views.home , name="home"),
   
   path('vehicle', views.vehicle , name="vehicle"),

   path('rental', views.rental , name="rental"),

   path('add_vehicle' , views.add_vehicle , name= "add_vehicle"),

   path('add_rental' , views.add_rental , name= "add_rental"),
]
