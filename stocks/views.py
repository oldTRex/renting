import json
import re
from django.http import request
import requests

from django.shortcuts import render

# Create your views here.


def home(request):
    # sandbox_c7grba2ad3ibsjtt23pg
    token = "sandbox_c7grba2ad3ibsjtt23pg"
    if request.method == 'POST':
        ticker = request.POST['ticker']
        ticker = ticker.upper()
       
        url = "https://finnhub.io/api/v1/quote?symbol=" + ticker + "&token=" + token
        api_request = requests.get(url)
        print(url)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."

        return render(request, "home.html", {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a stock symbol !"})

    


def about(request):
    return render(request, 'about.html', {})
