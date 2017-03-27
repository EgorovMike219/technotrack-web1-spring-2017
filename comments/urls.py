from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', CommentView.as_view(), name="comment"),
    url(r'^(?P<pk>\d+)/edit/$', login_required(UpdateComment.as_view()), name="update_comment"),
]