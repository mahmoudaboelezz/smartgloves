from multiprocessing import context
from urllib import response
from django.shortcuts import render
from .models import *
import requests
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    members = Names.objects.all()
    return render(request, 'home.html',{'members':members , })

def connect(request):
    return render(request, 'connect.html')

def output(request):
    if request.method == 'GET':
        # get data from form
        print(f'{request.POST},req')
    data = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    
    return render(request, 'output.html',context={'data':data[0:1]})

def speech(request):
    # query in models.related_word to get the related words
    if request.method == 'GET':
        data = request.POST.get('value')
        lookup = RelatedWord.objects.filter(word__icontains=data)
        return JsonResponse({'data':lookup})
        
    return render(request, 'speech.html')

def setting(request):
    return render(request, 'setting.html')

def location(request):
#     # get location on map longitude and latitude
#     from geopy.geocoders import Nominatim
#     loc = Nominatim(user_agent="GetLoc")
#     getloc = loc.geocode('egypt')
#     print(getloc.latitude, getloc.longitude)
#     import geocoder
#     g = geocoder.ip('me')
#     print(g.latlng)
#     import json
#     from urllib.request import urlopen
    
#     url = 'http://ip-api.com/json'
#     response = urlopen(url)
#     data = json.loads(response.read())
#     print(data)
    return render(request, 'location.html')

def test(request):
    # print result from ajax request
    if request.method == 'POST':
        # get data from ajax request and add it to context
        data = request.POST.get('value')
        print(data)
        from django.http import JsonResponse
        return JsonResponse({'data':data+'test'})

    return render(request, 'test.html')