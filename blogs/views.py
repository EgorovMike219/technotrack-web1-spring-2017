# coding: utf-8

from django.http import Http404
from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Blog, Post
from comments.models import Comment


class SortForm(forms.Form):

    sort = forms.ChoiceField(
        choices=(
            ('title', u'Заголовок'),
            ('description', u'Описание'),
            ('rate', u'Рейтинг'),
        ), required=False
    )
    search = forms.CharField(required=False)


class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    model = Blog
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(BlogList, self).get_queryset()
        if self.sortform.is_valid():
            if self.sortform.cleaned_data['sort']:
                qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['sortfrom'] = self.sortform
        return context


class UpdateBlog(UpdateView):
    template_name = 'blogs/add_blog.html'
    model = Blog
    fields = ('title', 'description', 'category')
    success_url = reverse_lazy('blogs:blog_list')


class CreateBlog(CreateView):
    template_name = 'blogs/add_blog.html'
    model = Blog
    fields = ('title', 'description', 'category')
    success_url = reverse_lazy('blogs:blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreateBlog, self).form_valid(form)


class PostList(ListView):
    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(PostList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        blog = Blog.objects.filter(id=self.kwargs.get('blog_id')).first()
        if blog == None:
            raise Http404
        qs = super(PostList, self).get_queryset().filter(blog=blog)
        if self.sortform.is_valid():
            if self.sortform.cleaned_data['sort']:
                qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.filter(id=self.kwargs.get('blog_id')).first()
        context['sortfrom'] = self.sortform
        return context

    template_name = "blogs/post_list.html"
    model = Post
    queryset = Post.objects.all()


class UpdatePost(UpdateView):
    template_name = 'blogs/add_post.html'
    model = Blog
    fields = ('title', 'description')
    success_url = reverse_lazy('blogs:blog_list')


class CreatePost(CreateView):
    template_name = 'blogs/add_post.html'
    model = Post
    fields = ('title', 'description', 'blog')
    success_url = reverse_lazy('blogs:blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreatePost, self).form_valid(form)


class PostView(CreateView):
    template_name = 'blogs/post.html'
    model = Comment
    fields = ('description',)
    success_url = reverse_lazy('blogs:blog_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        form.instance.post = Post.objects.filter(id=self.kwargs.get('pk')).first()
        return super(PostView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.filter(id=self.kwargs.get('pk')).first()
        return context


class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = "blogs/blog.html"