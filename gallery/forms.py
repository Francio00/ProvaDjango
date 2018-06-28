from django import forms
from .models import Photo, Video

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=('img','title','text',)

class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=('url', 'title','text',)
