from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import *

class CommentView(DetailView):
    queryset = Comment.objects.all()
    template_name = "comments/comment.html"