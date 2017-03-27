

# Create your views here.
from django.http import Http404
from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Comment



class CommentView(DetailView):
    queryset = Comment.objects.all()
    template_name = "comments/comment.html"


class UpdateComment(UpdateView):
    template_name = 'comments/update_comment.html'
    model = Comment
    fields = ('description',)
    success_url = reverse_lazy('blogs:blog_list')


class CreateComment(CreateView):
    template_name = 'comments/add_comment.html'
    model = Comment
    fields = ('description', 'post',)
    success_url = reverse_lazy('blogs:blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreateComment, self).form_valid(form)
