
import imp
import json
from time import sleep
from urllib import response
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .serializer import HandGestureSerializer
from .models import *
import requests
from django.http import JsonResponse
from .forms import ReadImagesForm
import pyocr
# Create your views here.
def homepage(request):
    members = Names.objects.all()
    return render(request, 'home.html',{'members':members , })

def connect(request):
    site = 'https://youtu.be/dQw4w9WgXcQ'
    check = requests.get(site)
    if check.status_code == 200:
        return render(request, 'connect.html',{'site':site})
    else:
        return render(request, 'connect.html')
    
    

def output(request):
    if request.method == 'GET':
        # get data from form
        print(f'{request.POST},req')
    data = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    
    return render(request, 'output.html',context={'data':data[0:1]})

def speech(request):
    # query in models.related_word to get the related words
    # if request.method == 'GET':
    #     data = request.POST.get('value')
    #     lookup = HandGesture.objects.filter()
    #     return JsonResponse({'data':lookup})
        # translate the word from arabic to english
        # word = request.POST.get('value')
        # print(word)
        # if word :
        #     import pyttsx3
        #     engine = pyttsx3.init()
        #     engine.say(word)
        #     engine.runAndWait()
        #     return JsonResponse({'data':word})
    
        
    return render(request, 'speech.html')

def setting(request):
    
    ####################
    nodeip = NodeMcu.objects.get(id=1)
    getnewnode = request.POST.get('newnode')
    
    form = ReadImagesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        # get image after saving it
        lang = request.POST.get('lang')
        image = Read_images.objects.last()
        read = pyocr.ocrtest(image.image, lang)
        print(read)
        # convert the array to string
        str1 = ''
        for i in read:
            str1 += i + ' '
        print(str1)
        # add str1 to the database
        Read_images.objects.filter(id=image.id).update(text=str1)
        return redirect('/setting/')
    if getnewnode:
        print(getnewnode)
        nodeip.ip_address = getnewnode
        nodeip.save()
        return redirect('/speech')
        
    return render(request, 'setting.html',{'nodeip':nodeip, 'form':form})

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
    if request.method == 'GET':
        url = 'http://192.168.235.135/read'
        request = requests.get(url)
        # send the data to the ajax request
        data = request.json()
        # print the key of 'f1h2' in the data
        print(data['f1h1'], data['f2h1'],data['f3h1'],data['f4h1'],data['f5h1'],data['f1h2'],data['f2h2'],data['f3h2'],data['f4h2'],data['f5h2'],data['gyro'])
        # check if the data is the same as the previous data
        list = [data['f1h1'], data['f2h1'],data['f3h1'],data['f4h1'],data['f5h1'],data['f1h2'],data['f2h2'],data['f3h2'],data['f4h2'],data['f5h2'],data['gyro']]
        if data['f1h1'] == list[0] and data['f2h1'] == list[1] and data['f3h1'] == list[2] and data['f4h1'] == list[3] and data['f5h1'] == list[4] and data['f1h2'] == list[5] and data['f2h2'] == list[6] and data['f3h2'] == list[7] and data['f4h2'] == list[8] and data['f5h2'] == list[9] and data['gyro'] == list[10]:
            sleep(.5)
            data['f1h1'] = list[0] and data['f2h1'] == list[1] and data['f3h1'] == list[2] and data['f4h1'] == list[3] and data['f5h1'] == list[4] and data['f1h2'] == list[5] and data['f2h2'] == list[6] and data['f3h2'] == list[7] and data['f4h2'] == list[8] and data['f5h2'] == list[9] and data['gyro'] == list[10]
            print('same')
        related_word = HandGesture.objects.filter(f1h1=data['f1h1'], f2h1=data['f2h1'],f3h1=data['f3h1'],f4h1=data['f4h1'],f5h1=data['f5h1'],f1h2=data['f1h2'],f2h2=data['f2h2'],f3h2=data['f3h2'],f4h2=data['f4h2'],f5h2=data['f5h2'],accelerometer=data['gyro'])
        if related_word:
            print(related_word[0].related_word)
            return JsonResponse({'data':related_word[0].related_word,'longitude':data['long'],'latitude':data['lat']})
        else:
            return JsonResponse({'data':'not found'})
        # print(related_word[0].related_word)
        # # print(related_word)
        # return JsonResponse({'data':related_word[0].related_word})
    if request.method == 'POST':
        url = 'http://192.168.235.135/read'
        request = requests.get(url)
        data = request.json()
        print(data['long'], data['lat'])
        return JsonResponse({'data':data['long'], 'data2':data['lat']})

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
        
        data = HandGesture.objects.filter(accelerometer=self.request.GET.get('accelerometer'),
                                          f1h1=self.request.GET.get('f1h1')
                                          ,f2h1=self.request.GET.get('f2h1')
                                          ,f3h1=self.request.GET.get('f3h1')
                                          ,f4h1=self.request.GET.get('f4h1')
                                          ,f5h1=self.request.GET.get('f5h1')
                                          ,f1h2=self.request.GET.get('f1h2')
                                          ,f2h2=self.request.GET.get('f2h2'),
                                          f3h2=self.request.GET.get('f3h2')
                                          ,f4h2=self.request.GET.get('f4h2')
                                          ,f5h2=self.request.GET.get('f5h2'))
                                          
        # print the related_word in data
        for i in data:
            print(i.related_word)

            
        # only return the word
        return data
    




#test
    
