from django.contrib import admin

# Register your models here.
from .models import Post, Blog

admin.site.register(Post)
admin.site.register(Blog)