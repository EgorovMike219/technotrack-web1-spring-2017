from django.db import models
from django.conf import settings
# Create your models here.


class Comment(models.Model):
    #а вот собственно привязка камента к посту
    post = models.ForeignKey('blogs.Post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField(max_length=1000)
    rate = models.IntegerField()

    def __str__(self):
        return self.description[:30]
