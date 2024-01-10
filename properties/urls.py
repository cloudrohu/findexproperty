from django.urls import path

from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('manage-land/', views.manage_land, name='manage-land'),
    path('manage-commercial-sell/', views.manage_commercial_sell, name='manage-commercial-sell'),
    path('manage-commercial-rent/', views.manage_commercial_rent, name='manage-commercial-rent'),
    path('manage-residential-sell/', views.manage_residential_sell, name='manage-residential-sell'),
    path('manage-residential-rent/', views.manage_residential_rent, name='manage-residential-rent'),
    path('manage-pg/', views.manage_pg, name='manage_pg'),

    path('post-land/', views.post_land, name='post-land'),
    path('post-commercial-sell/', views.post_commercial_sell, name='post-commercial-sell'),
    path('post-commercial-rent/', views.post_commercial_rent, name='post-commercial-rent'),
    path('post-residential-sell/', views.post_residential_sell, name='post-residential-sell'),
    path('post-residential-rent/', views.post_residential_rent, name='post-residential-rent'),
    path('post-pg/', views.post_pg, name='post-pg'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)