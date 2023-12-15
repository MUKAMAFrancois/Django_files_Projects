from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class TechRelated(models.Manager):
    def get_queryset(self):
        return super(TechRelated,self).get_queryset().filter(status='tech')
class Post(models.Model):
    tags=TaggableManager()
    objects=models.Manager() # default manager
    tech=TechRelated() # our custom manager
    #
    category_choices=(('business','BUSINESS'),
                      ('tech','TECHNOLOGY'),
                      ('sports','SPORTS'),
                      ('health','HEALTH'),
                      ('sciences','SCIENTIC'),
                      ('travel','TRAVEL'),
                      ('politics','POLITICS'),
                      ('news','NEWS'),
                      ('rest','OTHERS'))
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, unique_for_date='publish')
    publish=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    img=models.ImageField(upload_to='media/',default='', blank=True)

    # upload to is a subdirectory to store images.
    # You need to install "Pillow" dependency
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='my_posts')
    category=models.CharField(max_length=100, choices=category_choices,default='news')

    class Meta:
        ordering=('-publish',)
    
    def __str__(self):
        return self.title

class CommentModel(models.Model):
    apost=models.ForeignKey(Post,on_delete=models.DO_NOTHING,related_name='commented')
    name=models.CharField(max_length=233)
    content=models.TextField()
    email=models.EmailField(default='your_email@you.co')
    company=models.URLField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return f'Comments by {self.name} on {self.apost}'


