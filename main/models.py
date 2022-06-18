import uuid
from django.db import models

# Create your models here.
class Names(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Team Members"

class HandGesture(models.Model):
    # we have 10 resistors in both hands detected by the glove to be able to detect the gesture
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    f1h1 = models.IntegerField(default=0)
    f2h1 = models.IntegerField(default=0)
    f3h1 = models.IntegerField(default=0)
    f4h1 = models.IntegerField(default=0)
    f5h1 = models.IntegerField(default=0)
    f1h2 = models.IntegerField(default=0)
    f2h2 = models.IntegerField(default=0)
    f3h2 = models.IntegerField(default=0)
    f4h2 = models.IntegerField(default=0)
    f5h2 = models.IntegerField(default=0)
    

    def __str__(self):
        # only show the first 5 digits of the uuid
        return str(self.uuid)[:5]
    class Meta:
        verbose_name_plural = "Hand Gesture"
        
class RelatedWord(models.Model):
    # can be related to signle foreign key
    word = models.CharField(max_length=200)
    handgesture = models.OneToOneField(HandGesture, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.word
    
    class Meta:
        verbose_name_plural = "Related Word"
        
class Emergency(models.Model):
    send_location = models.BooleanField(default=False)
    emergency_number = models.CharField(max_length=100, default='911')
    # location_altitude = models.IntegerField(default=0)
    # location_latitude = models.IntegerField(default=0)
    HandGesture = models.OneToOneField(HandGesture, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.emergency_number} {self.HandGesture}'
    
    class Meta:
        verbose_name_plural = "Emergency"
        
class Battery(models.Model):
    lhbattery= models.IntegerField(default=0)
    rhbattery= models.IntegerField(default=0)
    def __str__(self):
        return f'{self.lhbattery} {self.rhbattery}'
    
    class Meta:
        verbose_name_plural = "Battery"
        
class Reset(models.Model):
    reset = models.BooleanField(default=False)
    HandGesture = models.OneToOneField(HandGesture, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.reset}'
    
    class Meta:
        verbose_name_plural = "Reset"