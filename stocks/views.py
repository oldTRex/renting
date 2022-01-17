import json
from django.http import request 
import requests

from django.shortcuts import render

# Create your views here.


def home(request):
   # sandbox_c7grba2ad3ibsjtt23pg
   
    token = "sandbox_c7grba2ad3ibsjtt23pg"
    url = "https://finnhub.io/api/v1/quote?symbol=AAPL&token=" + token
    api_request = requests.get(url)
    
    try:
        api = json.loads(api_request.content)
    except Exception as e :
        api = "Error.."


    return render(request , "home.html" ,{'api':api})


def about (request):
    return render(request, 'about.html', {})

