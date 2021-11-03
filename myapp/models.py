from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 



# Create your models here.

choices = [
    ('In jail','In jail'),('Police custady','police custady'),('escaping','escaping')
]

class Tourism(models.Model):
    place = models.CharField(max_length=200,blank=True,null=True)
    title = models.CharField(max_length=400)
    image = models.ImageField(null = True,blank = True,upload_to='images/')
    details = RichTextUploadingField()
    
    # name = models.CharField(max_length = 255)
    # incident_date = models.DateTimeField( auto_now=False, auto_now_add=False)
    # village = models.CharField(max_length = 100)
    # district = models.CharField(max_length=100)
    # author = models.ForeignKey(User,default='',  on_delete=models.CASCADE)
    # victim = models.CharField(max_length = 255)
    # punishment = models.CharField(max_length = 400)
    # status = models.CharField(max_length = 255,choices=choices,default=1)
    def __str__(self):
        return self.place  

    def get_absolute_url(self):
        return reverse("rapist-detail", args = str(self.id))
    

