
from rest_framework import serializers
from .models import *
from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

class HandGestureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandGesture
        fields = '__all__'
        filter_fields = '__all__'
        search_fields = '__all__'
        # enable get by accelerometer value
        lookup_field = 'accelerometer'
        # search
        
@api_view(['GET'])
def get_handgesture(request):
    if request.method == 'GET':
        # get data from form
        print(f'{request.GET},req')
        data = HandGesture.objects.all()
        serializer = HandGestureSerializer(data, many=True)
        return Response(serializer.data)

