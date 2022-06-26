from django.urls import include, path
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.homepage, name='home'),
    path('connect/', views.connect, name='connect'),
    path('output/', views.output, name='output'),
    path('speech/', views.speech, name='speech'),
    path('setting/', views.setting, name='setting'),
    path('location/', views.location, name='location'),
    path('test/', views.test, name='test'),
    
]
