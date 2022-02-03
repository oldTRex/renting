
from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import is_valid_path

from vehicle.forms import RentalForm
from .models import Vehicle, Rental
from decimal import Decimal
import datetime


# Create your views here.

def home(request):

    return render(request, 'home.html', {'ticker': "Enter a vehicle symbol !"})


def vehicle(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        color = request.POST.get('color')
        model = request.POST.get('model')
        price = Decimal(request.POST.get('price') or '1')
        vehicle = Vehicle.objects.create(
            name=name, color=color, model=model, price=price)

        messages.success(request, (vehicle.name + " has been added"))

        return redirect('vehicle')
    else:
        vehicles = Vehicle.objects.all()
         
        return render(request, 'vehicle.html', {'vehicles': vehicles})


def rental(request):
    vehicles = Vehicle.objects.all()
    
    if request.method == 'POST':

        form = RentalForm(request.POST or None)
        # v1 = request.POST['vehicle']
        
        if form.is_valid():
            form.save()
            
            messages.success(request, (" rental has been added"))

        messages.success(request, (form.errors))
        return redirect('rental')
    else:
        rentals = Rental.objects.all()

        return render(request, 'rental.html', {'rentals': rentals, 'vehicles': vehicles})


def delete_vehicle(request, vehicle_id):
    item = Vehicle.objects.get(pk=vehicle_id)
    item.delete()
    messages.success(request, ("vehicle has been deleted!"))
    return redirect('vehicle')


def delete_rental(request, rental_id,):
    item = Rental.objects.get(pk=rental_id)
    item.delete()
    messages.success(request, ("rental has been deleted!"))
    return redirect('rental')
