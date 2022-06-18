import uuid
from django.db import models

# Create your models here.
class Names(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class HandGesture(models.Model):
    # we have 10 resistors in both hands detected by the glove to be able to detect the gesture
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    f1h1 = models.FloatField(default=0)
    f2h1 = models.FloatField(default=0)
    f3h1 = models.FloatField(default=0)
    f4h1 = models.FloatField(default=0)
    f5h1 = models.FloatField(default=0)
    f1h2 = models.FloatField(default=0)
    f2h2 = models.FloatField(default=0)
    f3h2 = models.FloatField(default=0)
    f4h2 = models.FloatField(default=0)
    f5h2 = models.FloatField(default=0)
    

    def __str__(self):
        return self.uuid
    class Meta:
        verbose_name_plural = "HandGesture"
        
class RelatedWord(models.Model):
    word = models.CharField(max_length=100)
    HandGesture = models.ForeignKey(HandGesture, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.word
    
    class Meta:
        verbose_name_plural = "RelatedWord"
        
class Emergency(models.Model):
    emergency_number = models.CharField(max_length=100)
    location_altitude = models.FloatField(default=0)
    location_latitude = models.FloatField(default=0)
    HandGesture = models.ForeignKey(HandGesture, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.emergency_number} {self.current_location}'
    
    class Meta:
        verbose_name_plural = "Emergency"
        
class Battery(models.Model):
    lhbattery= models.FloatField(default=0)
    rhbattery= models.FloatField(default=0)
    def __str__(self):
        return f'{self.lhbattery} {self.rhbattery}'
    
    class Meta:
        verbose_name_plural = "Battery"