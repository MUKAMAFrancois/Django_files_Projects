from django.db import models

# Create your models here.

class Services(models.Model):
    #icon=models.ImageField()
    title=models.CharField(max_length=40)
    description=models.TextField()
    is_popular=models.BooleanField(default=True)

    def __str__(self):
        return self.title