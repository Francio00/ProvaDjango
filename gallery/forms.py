from django import forms
from .models import Post, Comments

class MediaForm(forms.ModelForm)
    class Meta:
        model=Media
        fields=('author','description',)

