from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy
from profiles.forms import User, UserInfoForm, UserProfileForm
from profiles.models import UserProfile
from django.shortcuts import redirect

# Create your views here.


class UserProfileCreateView(CreateView, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "profiles/user_info.html"
    success_url = reverse_lazy("profile:profile")

    def get(self, request):
        try:
            self.model.objects.get(basic_info=self.request.user)
        except:
            self.model.objects.create(basic_info=self.request.user)
        return super().get(request)

    def get_object(self, queryset=None):
        obj = self.model.objects.get(basic_info=self.request.user)
        return obj

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class UserProfileView(DetailView):
    model = UserProfile
    template_name = "profiles/profiles.html"

    def get_object(self, queryset=None):
        user = self.request.user
        try:
            obj = UserProfile.objects.get(basic_info=user)
            return obj
        except Exception:
            print("User object has not been populated yet, you may  need to  visit the user_profile form site once")


class UserInfoView(UpdateView):
    template_name = "profiles/user_info.html"
    form_class = UserInfoForm
    model = User
    success_url = reverse_lazy("profile:profile")

    def get_object(self, queryset=None):
        pk = self.request.user.id
        queryset = self.model.objects.all()
        obj = queryset.get(pk=pk)
        return obj
