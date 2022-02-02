from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {'ticker': "Enter a vehicle symbol !"})


def vehicle(request):
    return render(request, 'vehicle.html', {'ticker': "Enter a vehicle symbol !"})



def rental(request):
    return render(request, 'rental.html', {'ticker': "Enter a vehicle symbol !"})



def add_vehicle(request):
    return render(request, 'add_vehicle.html', {'ticker': "Enter a vehicle symbol !"})



def add_rental(request):
    return render(request, 'add_rental.html', {'ticker': "Enter a vehicle symbol !"})

    
    
