from django import forms
from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("background_dp", "dp", "bio", "role", "tech1", "tech2")
