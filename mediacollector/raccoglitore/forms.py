from django import forms
from .models import Post, Comments

class MediaForm(forms.ModelForm)
    class Meta:
        model=Media
        fields=('author','description',)

class CommentForm(forms.ModelForm):
    """docstring for CommentForm"""
    class Meta:
        model=Comments
        fields=('comment','author',)

