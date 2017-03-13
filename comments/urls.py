from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^(?P<pk>\d+)/', CommentView.as_view(), name = "comment")
]