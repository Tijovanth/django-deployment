from django.db import models

# Create your models here.
class Registration(models.Model):
    FirstName=models.CharField(max_length=264)
    LastName=models.CharField(max_length=264)
    Email=models.EmailField(unique=True,max_length=264)
    Portfolio=models.URLField(blank=True)
    Profilepic=models.ImageField(upload_to="profile_pics",blank=True)
