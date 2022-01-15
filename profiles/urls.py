from django.urls import path
from . import views

app_name = "profile"
urlpatterns = [
    # profile:profile
    path("view/", views.ProfileView.as_view(), name="profile"),
    path("edit/user-info", views.UserInfoView.as_view(), name="user_info"),
]
