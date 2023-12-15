from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager # for tagging
#from taggit.managers import TaggableManager

# managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

# create your models here

class Post(models.Model):
    #tags=TaggableManager()
    status_choices=(
        ('draft','Draft'),
        ('published','Published'),
    )

    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=250, unique_for_date='publish')
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10, choices=status_choices, default='draft')
    tags=TaggableManager() # for tagging


    class Meta:
        ordering=('-publish',)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blogapp1:post_detail',args=[self.publish.year,
                self.publish.month,
                self.publish.day, 
                self.slug])
        

    objects=models.Manager()
    published=PublishedManager()



# creating a Commenting System

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=200)
    email=models.EmailField(default='youremail@mail.com')
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('created',)
    
    def __str__(self):
        return f' Comments by {self.name} on {self.post} '
    
