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

def my_account(request):
    return render(request,'dashboard/base/sidebar_menu.html')
#------------------------------------------------------------------------------------------------------------------------------

def manage_commercial_sell(request): 
    return render(request,'dashboard/manage_properties/sell/commercial.html')

def manage_commercial_rent(request): 
    return render(request,'dashboard/manage_properties/rent/commercial.html')


def manage_residential_sell(request): 
    return render(request,'dashboard/manage_properties/sell/residential.html')

def manage_residential_rent(request): 
    return render(request,'dashboard/manage_properties/rent/residential.html')

def manage_pg(request): 
    return render(request,'dashboard/manage_properties/pg/postpg.html')

def manage_land(request): 
    return render(request,'dashboard/manage_properties/land.html')
#------------------------------------------------------------------------------------------------------------------------------

def post_commercial_sell(request): 
    return render(request,'dashboard/post_properties/sell/commercial.html')

def post_commercial_rent(request): 
    return render(request,'dashboard/post_properties/rent/commercial.html')


def post_residential_sell(request): 
    return render(request,'dashboard/post_properties/sell/residential.html')

def post_residential_rent(request): 
    return render(request,'dashboard/post_properties/rent/residential.html')

def post_pg(request): 
    return render(request,'dashboard/post_properties/pg/postpg.html')

def post_land(request): 
    return render(request,'dashboard/post_properties/land.html')

#___________________________________________________________________________________________________________
