from django.shortcuts import render
from .models import Post
from rest_framework.views import APIView


# Create your views here.

def index(request):
    my_post = Post.objects.all()
    return render(request, 'blog/index.html', {'my_post': my_post})

