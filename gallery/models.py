from django.db import models
from django.utils import timezone
# Create your models here.

class Media(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=240)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.description


# class Photo(Media):
#     #come mettere un'immagine?
#     pass

# class Video(Media):
#     #come mettere un video?
#     pass