from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^photo/$', views.media_list, name='photo_list'),
    url(r'^photo/(?P<pk>\d+)/$', views.media_details, name='photo_detail'),
    url(r'^photo/new/$', views.media_new, name='photo_new'),
    url(r'^photo/(?P<pk>\d+)/edit/$', views.media_edit, name='photo_edit'),
    url(r'^photo/(?P<pk>\d+)/delete/$', views.media_delete, name='photo_delete'),

    url(r'^video/$', views.media_list, name='video_list'),
    url(r'^video/(?P<pk>\d+)/$', views.media_details, name='video_detail'),
    url(r'^video/new/$', views.media_new, name='video_new'),
    url(r'^video/(?P<pk>\d+)/edit/$', views.media_edit, name='video_edit'),
    url(r'^video/(?P<pk>\d+)/delete/$', views.media_delete, name='video_delete'),
]