from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe
# Create your models here.
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.text import slugify

from utility.models import Bank,Amenities,Bedroom,Bathroom,Bolconis,Other_Room,Furnishing,Parking,Floor,Willing_To_Rent_Out,Age_Of_Properties


class Possession_In(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title    

THEMES = (
        ('Theme1', 'Theme1'),
        ('Theme2', 'Theme2'),
        ('Theme3', 'Theme3'),
        ('Theme4', 'Theme4'),
        ('Theme5', 'Theme5'),
        
    )

class City(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(City ,self).save(*args , **kwargs)
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
class Locality(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE) #many to one relation with Brand

    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " " + self.city.title
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Locality ,self).save(*args , **kwargs)
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('locality_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

class Developer(models.Model):
    title = models.CharField(max_length=50,unique=True)
    contact_person = models.CharField(max_length=255,null=True , blank=True)
    contact_no = models.CharField(max_length=255,null=True , blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand    
    email = models.EmailField(null=True,blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE,null=True,blank=True) #many to one relation with Brand    
    address = models.CharField(max_length=500,null=True , blank=True)
    keywords = models.CharField(max_length=255,null=True , blank=True)
    description = models.TextField(max_length=5000,null=True , blank=True)
    image=models.ImageField(blank=True,upload_to='images/')
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Developer ,self).save(*args , **kwargs)

    def get_absolute_url(self):
        return reverse('developer_detail', kwargs={'slug': self.slug})
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

class Commercial_Project(MPTTModel):

    PROPERTY_TYPE = (
        ('Office Space', 'Office Space'),
        ('Shop/Showroom', 'Shop/Showroom'),
        ('Commercial Land', 'Commercial Land'),
        ('Warehouse/Godown', 'Warehouse/Godown'),
        ('Industrial Building', 'Industrial Building'),
        ('Industrial Shed', 'Industrial Shed'),
        
     )

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    Construction_Status = (
        ('Under Construction', 'Under Construction'),
        ('New Launch', 'New Launch'),
        ('Partially Ready To Move','Partially Ready To Move'),
        ('Ready To Move','Ready To Move'),  )

    
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE) #many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE) #many to one relation with Brand 
    propert_type=models.CharField(max_length=25, choices=PROPERTY_TYPE)   
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE) #many to one relation with Brand
    possession = models.ForeignKey(Possession_In, on_delete=models.CASCADE) #many to one relation with Brand    
    min_price = models.IntegerField(default=0,null=True,blank=True,)
    max_price = models.IntegerField(default=0,null=True,blank=True,)
    min_area = models.CharField(null=True,blank=True,max_length=50)
    max_area = models.CharField(null=True,blank=True,max_length=50)
    description = models.TextField(max_length=5000)    
    status=models.CharField(max_length=25, choices=STATUS)
    theme=models.CharField(max_length=25, choices=THEMES)    
    construction_status=models.CharField(max_length=25, choices=Construction_Status)
    image=models.ImageField(blank=True,upload_to='images/')
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Residential_Project ,self).save(*args , **kwargs)
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
class Residential_Project(MPTTModel):    
    
    PROPERTY_TYPE = (
        ('Residential Land', 'Residential Land'),
        ('Residential Apartment', 'Residential Apartment'),
        ('Independent House/Villa', 'Independent House/Villa'),
        ('Studio Apartment', 'Studio Apartment'),
        ('Independent/Builder Floor', 'Independent/Builder Floor'),
        ('Serviced Apartments', 'Serviced Apartments'),
        ('Farm House', 'Farm House'),
     )

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    Construction_Status = (
        ('Under Construction', 'Under Construction'),
        ('New Launch', 'New Launch'),
        ('Partially Ready To Move','Partially Ready To Move'),
        ('Ready To Move','Ready To Move'),
        )
    
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE) #many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE) #many to one relation with Brand 
    propert_type=models.CharField(max_length=25, choices=PROPERTY_TYPE)   
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE) #many to one relation with Brand
    possession = models.ForeignKey(Possession_In, on_delete=models.CASCADE) #many to one relation with Brand  
    min_price = models.IntegerField(default=0,null=True,blank=True,)
    max_price = models.IntegerField(default=0,null=True,blank=True,)
    min_area = models.CharField(null=True,blank=True,max_length=50)
    max_area = models.CharField(null=True,blank=True,max_length=50)  
    description = models.TextField(max_length=5000)    
    status=models.CharField(max_length=25, choices=STATUS)    
    theme=models.CharField(max_length=25, choices=THEMES)    
    construction_status=models.CharField(max_length=25, choices=Construction_Status)
    image=models.ImageField(blank=True,upload_to='images/')
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Residential_Project ,self).save(*args , **kwargs)
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

class Plat(MPTTModel):

    PROPERTY_TYPE = (
        ('Residential Plot', 'Residential Plot'),
        ('Commercial land','Commercial land'),
        ('Agricultural Land','Agricultural Land')
        
        
     )

    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    Construction_Status = (
        ('Under Construction', 'Under Construction'),
        ('New Launch', 'New Launch'),
        ('Partially Ready To Move','Partially Ready To Move'),
        ('Ready To Move','Ready To Move'),  )

    
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE) #many to one relation with Brand
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE) #many to one relation with Brand 
    propert_type=models.CharField(max_length=25, choices=PROPERTY_TYPE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE) #many to one relation with Brand
    possession = models.ForeignKey(Possession_In, on_delete=models.CASCADE) #many to one relation with Brand    
    description = models.TextField(max_length=5000)    
    status=models.CharField(max_length=25, choices=STATUS)    
    construction_status=models.CharField(max_length=25, choices=Construction_Status)
    image=models.ImageField(blank=True,upload_to='images/')
    slug = models.SlugField(unique=True , null=True , blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Residential_Project ,self).save(*args , **kwargs)
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

class Rproject_Images(models.Model):
    Residential_Project=models.ForeignKey(Residential_Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
class Cproject_Images(models.Model):
    Commercial_Project=models.ForeignKey(Commercial_Project,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    carpet_area = models.CharField(max_length=50,blank=True)
    floor_plan = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title 

class Rproject_Price(models.Model):
    Residential_Project=models.ForeignKey(Residential_Project,on_delete=models.CASCADE)
    price = models.CharField(max_length=50,blank=True)
    carpet_area = models.CharField(max_length=50,blank=True)
    floor_plan = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.price    
class Cproject_Price(models.Model):
    Residential_Project=models.ForeignKey(Residential_Project,on_delete=models.CASCADE)
    price = models.CharField(max_length=50,blank=True)
    carpet_area = models.CharField(max_length=50,blank=True)
    floor_plan = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.price    
    

class Cfacilities(models.Model):
    Commercial_Project=models.ForeignKey(Commercial_Project,on_delete=models.CASCADE)
    amenities=models.ForeignKey(Amenities,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.title
class Rfacilities(models.Model):
    Residential_Project=models.ForeignKey(Residential_Project,on_delete=models.CASCADE)
    amenities=models.ForeignKey(Amenities,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.title