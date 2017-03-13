from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    rate = models.IntegerField()

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey(Blog)
    title =models.CharField(max_length = 255)
    description = models.TextField()
    rate = models.IntegerField()

