from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


post = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_created': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_created': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': post
    } 
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})