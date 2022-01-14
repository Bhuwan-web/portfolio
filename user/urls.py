from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # accounts/signup
    # accounts:signup
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]
