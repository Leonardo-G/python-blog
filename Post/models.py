from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    summary = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="post", null = True, blank = True)
    created_post = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visited = models.IntegerField(default=0)
    
class Nosotros(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    camada = models.IntegerField()
    url = models.CharField(max_length=100)