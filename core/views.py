from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.http import HttpResponse
from django.views.generic import TemplateView
from blogs.models import *
from core.models import *
from comments.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class CreateUser(CreateView):
    form_class = MyUserCreationForm
    template_name = 'core/add_user.html'
    success_url = reverse_lazy('core:home')


class UpdateUser(UpdateView):
    form_class = MyUserChangeForm
    template_name = 'core/add_user.html'
    success_url = reverse_lazy('core:home')


def test(request):
    return HttpResponse("dfghjk")


class HomePageView(TemplateView):
    template_name = 'core/file.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['users'] = User.objects.all()
        context['blogs'] = Blog.objects.all()
        context['comments'] = Comment.objects.all()
        context['posts'] = Post.objects.all()
        return context
