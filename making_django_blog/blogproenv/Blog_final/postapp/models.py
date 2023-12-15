from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    content=HTMLField()
    sciences=models.BooleanField(default=False)
    likes=models.ManyToManyField(User,related_name='likes', blank=True)

