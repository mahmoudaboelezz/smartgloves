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
    # gesture_name = models.CharField(max_length=200,help_text="Enter the gesture name")
    # gesture_image = models.ImageField(upload_to='gesture_images/', blank=True)
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
    accelerometer = models.IntegerField(default=0)
    related_word = models.CharField(max_length=400, help_text="Enter the related word", blank=True)
    

    def __str__(self):
        # only show the first 5 digits of the uuid
        return f' {self.f1h1} {self.f2h1} {self.f3h1} {self.f4h1} {self.f5h1} {self.f1h2} {self.f2h2} {self.f3h2} {self.f4h2} {self.f5h2} , {self.accelerometer} , {self.related_word}'
    class Meta:
        verbose_name_plural = "Hand Gesture"
    
    # on save, update if read_images has text remove related word
   
# class RelatedWord(models.Model):
#     # can be related to signle foreign key
#     word = models.CharField(max_length=200)
#     handgesture = models.OneToOneField(HandGesture, on_delete=models.CASCADE)

    
#     def __str__(self):
#         return self.word
    
#     class Meta:
#         verbose_name_plural = "Related Word"
        
class Emergency(models.Model):
    send_location = models.BooleanField(default=False)
    emergency_number = models.CharField(max_length=100, default='911')

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
        
class NodeMcu(models.Model):
    # only contain ip adress once 
    ip_address = models.CharField(max_length=100)
    def __str__(self):
        return self.ip_address
    
    
    
class Read_images(models.Model):
    # only contain ip adress once 
    HandGesture = models.OneToOneField(HandGesture, on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    text = models.CharField(max_length=400, default='', blank=True)
    def __str__(self):
        return f'{self.image} {self.text}'
    
    class Meta:
        verbose_name_plural = "Read_images"
    
    # if save go update handgesture with text
    def save(self, *args, **kwargs):
    # go delete old handgesture
        # old = Read_images.objects.get(pk=self.pk)
        # if old.HandGesture:
        #     old.HandGesture.related_word = ''
        #     old.HandGesture.save()
        if self.HandGesture:
            self.HandGesture.related_word = self.text
            self.HandGesture.save()
            
        super(Read_images, self).save(*args, **kwargs)
        
    # if change handgesture reset text of handgesture
    def delete(self, *args, **kwargs):
        if self.HandGesture:
            self.HandGesture.related_word = ''
            self.HandGesture.save()
        super(Read_images, self).delete(*args, **kwargs)
    

    
        
    