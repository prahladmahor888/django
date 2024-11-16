from django.db import models

# Create your models here.
class UploadImage(models.Model):
    userid = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

class createuser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=200)

class cardEvent(models.Model):
    eventText = models.CharField(max_length=500)
    eventImage = models.ImageField(upload_to='events/')

class userInfo(models.Model):
    username = models.CharField(max_length=200, blank=True, unique=True)
    userAbout = models.CharField(max_length=500)
    userImage = models.ImageField(upload_to='user_images/')