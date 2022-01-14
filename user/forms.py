from django import forms
from django.contrib.auth import get_user_model
from django.forms import fields
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class ModelUserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
