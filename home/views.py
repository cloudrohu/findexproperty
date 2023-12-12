from django.shortcuts import render

# Create your views here.

from properties.models import Residential_Project
from .models import*

def index(request):
    slider = Slider.objects.all().order_by('-id')[:4]  #first 4 products    
    page="home"
    context={        
        'slider':slider,        
    }   

    return render(request,'index.html',context)

