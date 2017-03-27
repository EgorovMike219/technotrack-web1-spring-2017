from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^users/add/$', CreateUser.as_view(), name='add_user'),
    url(r'^users/edit/$', login_required(UpdateUser.as_view()), name='update_user'),
]