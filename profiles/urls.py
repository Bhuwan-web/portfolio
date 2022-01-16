from django.urls import path
from . import views

app_name = "profile"
urlpatterns = [
    # profile:profile
    path("view/", views.UserProfileView.as_view(), name="profile"),
    path("edit/user-info", views.UserInfoView.as_view(), name="user_info"),
    path("edit/user-profile", views.UserProfileCreateView.as_view(), name="user_profile"),
]
