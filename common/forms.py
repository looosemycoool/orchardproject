from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "username", "password1", "password2",)


# last_name이 이름
# username 이 아이디