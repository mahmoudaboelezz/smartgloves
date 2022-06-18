from django.contrib import admin
from .models import HandGesture, RelatedWord, Emergency, Names
# Register your models here.
admin.site.register(HandGesture, admin.ModelAdmin)
admin.site.register(Names)

class RelatedWordInline(admin.StackedInline):
    model = RelatedWord
    extra = 1

class EmergencyInline(admin.StackedInline):
    model = Emergency
    extra = 1
    
class HandGestureAdmin(admin.ModelAdmin):
    inlines = [RelatedWordInline, EmergencyInline]