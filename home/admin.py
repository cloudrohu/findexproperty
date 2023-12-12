from django.contrib import admin

# Register your models here.
from .models import*
class SliderAdmin(admin.ModelAdmin):
    list_display = ['image','name', 'line_1','line_2']
    
admin.site.register(Slider,SliderAdmin)