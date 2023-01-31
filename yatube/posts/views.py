from django.conf import settings
from django.shortcuts import render, get_object_or_404

from .models import Post, Group


# Главная страница
def index(request):
    template = 'posts/index.html'
    text = "Это главная страница проекта Yatube"
    posts = Post.objects.all()[:settings.NOM_POST]
    context = {
        'text': text,
        'posts': posts,
    }
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = "Здесь будет информация о группах проекта Yatube"
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.NOM_POST]
    context = {
        'text': text,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
