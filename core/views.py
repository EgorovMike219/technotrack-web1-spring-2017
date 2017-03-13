from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from blogs.models import *
from core.models import *
from comments.models import *
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
