from django.contrib import admin
from .models import HandGesture,  Emergency, Names , Battery, Reset,NodeMcu, Read_images
# Register your models here.

admin.site.register(Names)

# add emergency and reset and related word to hand gesture stack 
class ResetInline(admin.TabularInline):
    model = Reset
    extra = 1
    
class EmergencyInline(admin.TabularInline):
    model = Emergency
    extra = 1
    
class ReadImagesInline(admin.TabularInline):
    model = Read_images
    extra = 1

# class RelatedWordInline(admin.StackedInline):
#     model = RelatedWord
#     extra = 1

        

class HandGestureAdmin(admin.ModelAdmin):
    inlines = [ EmergencyInline, ResetInline, ReadImagesInline]
    list_display = ('uuid', 'f1h1', 'f2h1', 'f3h1', 'f4h1', 'f5h1', 'f1h2', 'f2h2', 'f3h2', 'f4h2', 'f5h2','__str__')
    search_fields = ('uuid', 'f1h1', 'f2h1', 'f3h1', 'f4h1', 'f5h1', 'f1h2', 'f2h2', 'f3h2', 'f4h2', 'f5h2')
    class Meta:
        verbose_name_plural = "HandGesture"
    # on save, update if read_images has text remove related word

admin.site.register(HandGesture, HandGestureAdmin)
# admin.site.register(RelatedWord)
admin.site.register(Emergency)
admin.site.register(Reset)
admin.site.register(Read_images)
        


class BatteryAdmin(admin.ModelAdmin):
    list_display = ('lhbattery', 'rhbattery')
    


admin.site.register(Battery, BatteryAdmin)
admin.site.register(NodeMcu)
    
# change the admin title
admin.site.site_header = 'SmartGloves Admin'
admin.site.site_title = 'Aboelezz'
admin.site.index_title = 'SmartGloves Project'

