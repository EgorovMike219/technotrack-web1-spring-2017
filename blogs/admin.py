from django.contrib import admin

# Register your models here.
from .models import Post, Blog, Category

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Category)