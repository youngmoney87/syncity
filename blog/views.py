from django.shortcuts import render
from django.http import HttpResponse
from . models import Post


posts = [
    {
    'author': 'ChrisM',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'March 13, 2019'
    },
    {
    'author': 'ChrisM2',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'March 13, 2019'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})