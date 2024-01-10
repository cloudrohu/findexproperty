
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import home
import properties
from home import views 
from properties import views as PropertiesViews

from user import views as UserViews
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('', include('home.urls')),
    path('', include('properties.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    
    path('jet/', include('jet.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    


    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)