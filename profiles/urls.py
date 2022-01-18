from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "profile"
urlpatterns = [
    # profile:profile
    path("view/", views.UserProfileView.as_view(), name="profile"),
    path("edit/user-info", views.UserInfoView.as_view(), name="user_info"),
    path("edit/user-profile", views.user_profile_edit_view, name="user_profile"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
