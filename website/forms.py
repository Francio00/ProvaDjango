from django import forms
from .models import Post, Comments
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text',)

class CommentForm(forms.ModelForm):
    """docstring for CommentForm"""
    class Meta:
        model=Comments
        fields=('comment','author',)

