# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from blogs.forms import SortForm, UpdateBlogForm, CreateBlogForm, UpdatePostForm, CreatePostForm, PostViewForm
from .models import Blog, Post, Like


class BlogList(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
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
    model = Blog
    form_class = UpdateBlogForm
    template_name = 'blogs/update_blog.html'
    success_url = reverse_lazy('blogs:blog_list')


class CreateBlog(CreateView):
    form_class = CreateBlogForm
    template_name = 'blogs/add_blog.html'
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
    template_name = 'blogs/update_post.html'
    form_class = UpdatePostForm
    model = Post
    success_url = reverse_lazy('blogs:blog_list')


class CreatePost(CreateView):
    form_class = CreatePostForm
    template_name = 'blogs/add_post.html'
    success_url = reverse_lazy('blogs:blog_list')

    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse('blogs:post_list', args=[self.kwargs.get('blog_id')])
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.filter(id=self.kwargs.get('blog_id')).first()
        return context

    def form_valid(self, form):
        blog = Blog.objects.filter(id=self.kwargs.get('blog_id')).first()
        form.instance.author = self.request.user
        form.instance.blog = blog
        form.instance.rate = 0
        return super(CreatePost, self).form_valid(form)


class PostView(CreateView):
    def get_success_url(self):
        return reverse('blogs:post', args=(self.object.post.id, ))

    template_name = 'blogs/post.html'
    form_class = PostViewForm

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


class PostLikeAjaxView(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        # Забираем из базы пост, который собираются лайкнуть
        self.post_object = get_object_or_404(Post, id=pk)
        return super(PostLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        if not self.post_object.like_set.filter(author=self.request.user).exists():  # нужно ли проверять что пользователь не аноним
            like = Like()
            like.author = self.request.user
            like.place = self.post_object
            like.save()
            self.post_object.rate = Like.objects.filter(place=self.post_object).count()
            blog = Blog.objects.filter(post=self.post_object).first()
            blog.rate += 1
            blog.save()
            self.post_object.save()
            # Сначала мы проверили, что лайка от этого юзера у поста еще нет
            # Теперь мы здесь должны создать лайк, и вернуть новое количество лайков у поста
        return HttpResponse(Like.objects.filter(place=self.post_object).count())
