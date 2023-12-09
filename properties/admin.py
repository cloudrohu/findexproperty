import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *



@admin_thumbnails.thumbnail('image')
class CityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions', 'indented_title', 'image_thumbnail',
                    'related_locality_count',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
       
        # Add non cumulative product count
        qs = City.objects.add_related_count(qs,
                 Locality,
                 'city',
                 'locality_count',
                 cumulative=False)
        return qs

    def related_locality_count(self, instance):
        return instance.locality_count
    related_locality_count.short_description = 'Related Locality (for this specific City)'



@admin_thumbnails.thumbnail('image')
class LocalityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions', 'indented_title', 'image_thumbnail',
                    'residential_project_count',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
       
        # Add non cumulative product count
        qs = Locality.objects.add_related_count(qs,
                 Residential_Project,
                 'locality',
                 'residential_project_count',
                 cumulative=False)
        return qs

    def residential_project_count(self, instance):
        return instance.residential_project_count
    residential_project_count.short_description = 'Related Project (for this specific Locality)'



admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Developer,)
admin.site.register(Residential_Project,)
admin.site.register(Possession_In,)
