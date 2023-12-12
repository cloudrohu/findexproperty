from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to='banner/img')
    name = models.CharField(max_length=250,null=True)
    line_1 = models.CharField(max_length=250,null=True)
    line_2 = models.CharField(max_length=250,null=True)   
    def __str__(self):
        return self.name