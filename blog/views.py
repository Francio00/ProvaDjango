from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comments
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_list= Comments.objects.filter(post=post)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
    else:
        form = CommentForm()


    return render(request, 'blog/post_detail.html', {'post': post, 'comment_list' : comment_list, 'form':form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form,'postID': post.pk})

def post_delete(request, pk):
    #cancello il post
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return render(request,'blog/deleted_post.html',{})

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
