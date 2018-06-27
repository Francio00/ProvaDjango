from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    """docstring for ClassName"""
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date = models.DateTimeField( default=timezone.now )
    published_date = models.DateTimeField( blank=True,null=True)
    text2=models.TextField( blank=True,null=True)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title+" "+str(self.create_date)

class Comments(models.Model):
    """docstring for ClassName"""
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    comment=models.TextField(blank=True,null=True)
    author=models.CharField(max_length=50,blank=True,default="anonymous")

    def __str__(self):
        return self.published_date+" "+self.author