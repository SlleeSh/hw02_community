from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Post, Group


# Главная страница
def index(request):
    template = 'posts/index.html'
    text = "Это главная страница проекта Yatube"
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'text': text,
        'posts': posts,
    }
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = "Здесь будет информация о группах проекта Yatube"
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'text': text,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)


def profile(request, username):
    count = Post.objects.filter(author__username=username).count()
    posts = Post.objects.filter(author__username=username)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author': username,
        'count': count
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    count = Post.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'count': count
    }
    return render(request, 'posts/post_detail.html', context)
