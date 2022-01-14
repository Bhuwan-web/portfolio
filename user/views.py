from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model

from user.forms import ModelUserSignupForm
from django.urls import reverse_lazy

User = get_user_model()
# Create your views here.
class SignupView(CreateView):
    """Create new users to make their own portfolio and showcase on their own"""

    model = User
    form_class = ModelUserSignupForm
    template_name = "user/accounts.html"
    extra_context = {"title": "Signup Form", "heading": "Signup Form", "submit": "Signup"}
    success_url = reverse_lazy("accounts:login")


class CustomLoginView(LoginView):
    model = User
    template_name = "user/accounts.html"
    next_page = reverse_lazy("home:profile")
    extra_context = {"title": "Login Form", "heading": "Login Form", "submit": "Login"}
