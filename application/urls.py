"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blogs.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^comment/', include('comments.urls', namespace="comments")),
    #url(r'^posts/', include('blogs.urls', namespace="posts")),
    url(r'^posts/(?P<blog_id>\d+)/', PostList.as_view(), name = "post_list"),
    url(r'^post/(?P<pk>\d+)/', PostView.as_view(), name = "post"),
    url(r'^blogs/', include('blogs.urls', namespace="blogs")),
    url(r'^blog/(?P<pk>\d+)/', BlogView.as_view(), name="blog"),
    url(r'^core/', include('core.urls', namespace="core")),
    url(r'^$', include('core.urls', namespace="core")),
]
