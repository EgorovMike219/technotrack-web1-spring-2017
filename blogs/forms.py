from django import forms
from .models import Blog, Post
from comments.models import Comment


class SortForm(forms.Form):

    sort = forms.ChoiceField(
        choices=(
            ('title', u'Заголовок'),
            ('description', u'Описание'),
            ('rate', u'Рейтинг'),
        ), required=False
    )
    search = forms.CharField(required=False)


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category',)


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category',)


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description',)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', )


class PostViewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)