from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', BlogList.as_view(), name = "blog_list"), #в шаблоне ссылку на этот контроллер можно будет получить с помощью {% url "blog_list" %}
]
