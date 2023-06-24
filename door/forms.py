from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        help_text='',
    )
    username = forms.CharField(
        label='Имя',
        strip=False,
        help_text='',
    )

    class Meta:
        model = User
        fields = ('username', 'password1')