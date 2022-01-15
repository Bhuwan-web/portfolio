from django.urls import path
from . import views

app_name = "home"


urlpatterns = [
    # localhost:8000/
    # home:
    path("", views.ProfileView.as_view(), name="home"),
]
