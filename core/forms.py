from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import get_user_model



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class MyUserChangeForm(PasswordChangeForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(MyUserChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2')
