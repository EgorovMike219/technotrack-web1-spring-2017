from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, default='Общее')
    #overcategory = models.ForeignKey(Category)

    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()

    def __str__(self):
        return self.title


class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Post)