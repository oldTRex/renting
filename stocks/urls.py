from unicodedata import name
from django.urls import  include , path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
   path('', views.home , name="home"),
   
   path('about', views.about , name="about"),
]
