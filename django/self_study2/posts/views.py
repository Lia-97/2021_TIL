from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.decorators.http import require_POST,require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    # 
    return render(request, 'posts/main.html')


def index(request):
    posts = Post.objects.all().order_by('-pk')
    
    context = {
        'posts':posts,
    }

    return render(request, 'posts/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm
    comments = post.comment_set.all()
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments
    }

    return render(request, 'posts/detail.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('posts:index')


@login_required
@require_http_methods(['GET','POST'])
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/form.html', context)


@require_POST
def comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:detail', post.pk)
        context = {
            'comment_form': comment_form,
            'post':post,
        }
        return render(request, 'posts/detail.html', context)
    return redirect('accounts:login')
