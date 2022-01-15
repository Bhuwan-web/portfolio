from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from profiles.forms import User, UserInfoForm

# Create your views here.
class ProfileView(TemplateView):
    template_name = "profiles/profiles.html"


class UserInfoView(UpdateView):
    template_name = "profiles/user_info.html"
    form_class = UserInfoForm
    model = User
    success_url = reverse_lazy("home:profile")

    def get_object(self, queryset=None):
        pk = self.request.user.id
        queryset = self.model.objects.all()
        obj = queryset.get(pk=pk)
        return obj
