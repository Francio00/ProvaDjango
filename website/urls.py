from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'', include('blog.urls')),
    url(r'', include('gallery.urls')),
]