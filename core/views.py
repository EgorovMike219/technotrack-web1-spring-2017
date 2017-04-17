from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AnonymousUser

from django.http import HttpResponse
from django.views.generic import TemplateView
from blogs.models import *
from core.models import *
from comments.models import *
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from core.forms import *
from django.contrib.auth import get_user_model, authenticate, login


class CreateUser(CreateView):
    form_class = MyUserCreationForm
    template_name = 'core/add_user.html'
    success_url = reverse_lazy('core:home')


class UpdateUser(UpdateView):
    model = get_user_model()
    form_class = MyUserChangeForm
    #form_class = UserChangeForm
    template_name = 'core/update_user.html'
    success_url = reverse_lazy('core:home')

    def __init__(self): # не работает kwargs, request почему?
        super(UpdateUser, self).__init__()
        print(self.get_queryset())
        print(self.get_form_kwargs().get('pk'))
        user = get_user_model().objects.filter(id=self.kwargs.get('pk')).first()
        self.form_class = MyUserChangeForm(user)
        super(UpdateUser, self).__init__()


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


class Login(TemplateView):
    template_name = 'core/login.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Login, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['form'] = AuthenticationForm
        return context

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username', '')
        password = self.request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if (self.request.user.id is None) and (user is not None):
            login(self.request, user)
            return HttpResponse('ok')
        else:
            return HttpResponse('error')
