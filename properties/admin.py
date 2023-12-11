import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from . models import *



@admin_thumbnails.thumbnail('image')
class CityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions', 'indented_title', 'image_thumbnail',
                    'related_locality_count','residential_project_count',)
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
        qs = City.objects.add_related_count(qs,
                 Residential_Project,
                 'city',
                 'residential_project_count',
                 cumulative=False)
        return qs      
   
    def residential_project_count(self, instance):
        return instance.residential_project_count
    residential_project_count.short_description = 'Related Project (for this specific Locality)'
        

    def related_locality_count(self, instance):
        return instance.locality_count
    related_locality_count.short_description = 'Related Locality (for this specific City)'

@admin_thumbnails.thumbnail('image')
class LocalityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions','city', 'indented_title', 'image_thumbnail',
                    'residential_project_count',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    
    list_filter = ['city']
    
    
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

@admin_thumbnails.thumbnail('image')
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'contact_person','contact_no','email','address','locality','city','image_thumbnail']


@admin_thumbnails.thumbnail('image')
class Residential_ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','title','locality','city','propert_type', 'image_thumbnail']
    list_editable=('title','locality','city',) 
    list_filter = ('locality','city',) 
    search_fields = ('title','locality','city',)

@admin_thumbnails.thumbnail('image')
class Commercial_ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','title','locality','city','propert_type','image_thumbnail']
    list_editable=('title','locality','city',) 
    list_filter = ('locality','city',) 
    search_fields = ('title','locality','city',)




admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Residential_Project,Residential_ProjectAdmin)
admin.site.register(Commercial_Project,Commercial_ProjectAdmin)
admin.site.register(Possession_In,)
