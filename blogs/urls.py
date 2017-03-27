from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"), #в шаблоне ссылку на этот контроллер можно будет получить с помощью {% url "blog_list" %}
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="blog"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name="update_blog"),
    url(r'^add/$', login_required(CreateBlog.as_view()), name="add_blog"),
    url(r'^post/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name="update_post"),
    url(r'^posts/add/$', login_required(CreatePost.as_view()), name="add_post"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="post"),
    url(r'^posts/(?P<blog_id>\d+)/$', PostList.as_view(), name="post_list"),
]
