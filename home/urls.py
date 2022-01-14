from django.urls import path
from . import views

app_name = "home"


urlpatterns = [
    # localhost:8000/
    # home:
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
