from django.db import models
from django.utils import timezone
from blog.models import AbstractPost
# Create your models here.


class Photo(AbstractPost):
    img = models.FileField(upload_to='photos/')

class Video(AbstractPost):

    url=models.CharField(max_length=255)
    modified_url=models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        temp=self.url.split("/")
        temp_url=temp[-1]
        self.modified_url=temp_url.replace("watch?v=","")
        super(Model, self).save(*args, **kwargs)
