from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', BlogList.as_view(), name = "blog_list"), #в шаблоне ссылку на этот контроллер можно будет получить с помощью {% url "blog_list" %}
    url(r'^(?P<pk>\d+)/', BlogView.as_view(), name="blog"),
    url(r'^post/(?P<pk>\d+)/', PostView.as_view(), name = "post"),
    url(r'^posts/(?P<blog_id>\d+)/', PostList.as_view(), name = "post_list"),
]
