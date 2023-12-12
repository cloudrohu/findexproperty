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


class Bank(models.Model):
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title

class Amenities(models.Model):
    title = models.CharField(max_length=150,blank=True)
    icon = models.CharField(max_length=150,blank=True)
    
    def __str__(self):
        return self.title

class Bedroom(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Bathroom(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Bolconis(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Other_Room(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
class Furnishing(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
    
class Parking(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Floor(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Total_Floor(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title

class Willing_To_Rent_Out(models.Model):
    title = models.DateField(blank=True)    
    def __str__(self):
        return self.title

class Age_Of_Properties(models.Model):
    title = models.CharField(max_length=15,blank=True)    
    def __str__(self):
        return self.title
