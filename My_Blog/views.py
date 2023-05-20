from django.shortcuts import render
from .models import Post,Category
from rest_framework.views import APIView


# Create your views here.

def index(request):
    my_post = Post.objects.all()
    return render(request, 'blog/index.html', {'my_post': my_post})

def table(request):
    my_table = Category.objects.all()
    return render(request , "blog/table.html/", {"my_table":my_table})