from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Blog, Post
from django.shortcuts import get_object_or_404

class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    model = Blog

class PostList(ListView):
    template_name = "blogs/post_list.html"
    model = Post
    queryset = Post.objects.all()

class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = "blogs/blog.html"

class PostView(DetailView):
    queryset = Post.objects.all()
    template_name = "blogs/post.html"