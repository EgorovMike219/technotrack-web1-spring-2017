from django.conf.urls import url
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^users/add/$', CreateUser.as_view(), name='add_user'),
    url(r'^users/(?P<pk>\d+)/edit/$', login_required(UpdateUser.as_view()), name='update_user'),
]