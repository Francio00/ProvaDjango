from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import AbstractPost, Comments
from .models import Video, Photo
from .forms import VideoForm, PhotoForm
from django.http import HttpResponse


# Create your views here.
def comment_new(request):
    if request.method == "POST":
        form = CommentForm(request.COMMENT)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = "authorless"
            comment.published_date = timezone.now()
            comment.save()
            #return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    #return render(request, 'blog/post_edit.html', {'form': form})
from django.shortcuts import render

# Create your views here.
def media_new(request, pk):
    if "photo" in request.path:
        if request.method == "POST":
            form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.published_date = timezone.now()
            photo.save()
            return redirect('media_detail', pk=photo.pk)
        else:
            form = PhotoForm()
        return render(request, 'gallery/media_edit.html', {'form': form})

    elif "video" in request.path:
        if request.method == "POST":
            form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.published_date = timezone.now()
            video.save()
            return redirect('media_detail', pk=video.pk)
        else:
            form = VideoForm()
        return render(request, 'gallery/media_edit.html', {'form': form})

    else:
        return HttpResponse(status=404)


def media_edit(request, pk):
    if "photo" in request.path:
        photo = get_object_or_404(Photo, pk=pk)
        if request.method == "POST":
            form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.published_date = timezone.now()
            photo.save()
            return redirect('media_detail', pk=photo.pk)
        else:
            form = PhotoForm(instance=photo)
        return render(request, 'gallery/media_edit.html', {'form': form,'photoID': photo.pk})
    elif "video" in request.path:
        video = get_object_or_404(Video, pk=pk)
        if request.method == "POST":
            form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video.published_date = timezone.now()
            video.save()
            return redirect('media_detail', pk=video.pk)
        else:
            form = VideoForm(instance=video)
        return render(request, 'gallery/media_edit.html', {'form': form,'videoID': video.pk})
    else:
        return HttpResponse(status=404)


def media_list(request):
    if "photo" in request.path:
        photo= Photo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request,'gallery/media_list.html', {'photos': photo})
    elif "video" in request.path:
        video= Video.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request,'gallery/media_list.html', {'videos': video})
    else:
        return HttpResponse(status=404)


def media_details(request,pk):
    if "photo" in request.path:
        photo = get_object_or_404(Photo, pk=pk)
        comment_list= Comments.objects.filter(photo=photo)
        if request.method == "POST":
            form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo=photo
            comment.save()
        else:
            form = CommentForm()
            return render(request, 'gallery/media_detail.html', {'photo': photo, 'comment_list' : comment_list, 'form':form})
    elif "video" in request.path:
        video = get_object_or_404(Video, pk=pk)
        comment_list= Comments.objects.filter(video=video)

        if request.method == "POST":
            form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video=video
            comment.save()
        else:
            form = CommentForm()
        return render(request, 'gallery/media_detail.html', {'video': video, 'comment_list' : comment_list, 'form':form})
    else:
        return HttpResponse(status=404)


def media_delete(request,pk):
    if "photo" in request.path:
        photo=get_object_or_404(Photo,pk=pk)
        photo.delete()
        return render(request,'gallery/deleted_photo.html',{})
    elif "video" in request.path:
        video=get_object_or_404(Video,pk=pk)
        video.delete()
        return render(request,'gallery/deleted_video.html',{})
    else:
        return HttpResponse(status=404)

