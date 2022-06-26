
import json
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets

from .serializer import HandGestureSerializer
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
        lookup = HandGesture.objects.filter(word__icontains=data)
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

class viewsets_handgesture(viewsets.ModelViewSet):
    queryset = HandGesture.objects.all()
    serializer_class = HandGestureSerializer
    # enable get by accelerometer value
    lookup_field = 'accelerometer' 
    # enable search by params in url
    search_fields = '__all__'
    
    def get_queryset(self):
        # get data from form
        print(f'{self.request.GET},req')
        
        data = HandGesture.objects.filter(accelerometer=self.request.GET.get('accelerometer'),f1h1=self.request.GET.get('f1h1')
                                          ,f2h1=self.request.GET.get('f2h1'),f3h1=self.request.GET.get('f3h1'),f4h1=self.request.GET.get('f4h1'),f5h1=self.request.GET.get('f5h1')
                                          ,f1h2=self.request.GET.get('f1h2'),f2h2=self.request.GET.get('f2h2'),f3h2=self.request.GET.get('f3h2')
                                          ,f4h2=self.request.GET.get('f4h2'),f5h2=self.request.GET.get('f5h2'))
                                          
        # print the related_word in data
        for i in data:
            print(i.related_word)

            
        # only return the word
        return data





    
