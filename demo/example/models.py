from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
class Image(models.Model):
    alt = models.CharField(max_length=250)
    src = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)