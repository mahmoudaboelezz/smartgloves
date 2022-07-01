from django import forms
from .models import HandGesture, Emergency, Reset, Names, Battery, NodeMcu, Read_images

class ReadImagesForm(forms.ModelForm):
    class Meta:
        model = Read_images
        fields = ('image',)
        