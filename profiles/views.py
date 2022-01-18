from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy
from profiles.forms import User, UserInfoForm, UserProfileForm
from profiles.models import UserProfile
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

# Create your views here.


# class UserProfileCreateView(CreateView, UpdateView):
#     model = UserProfile
#     form_class = UserProfileForm
#     template_name = "profiles/user_info.html"
#     success_url = reverse_lazy("profile:profile")

#     def get(self, request):
#         try:
#             self.model.objects.get(basic_info=self.request.user)
#         except:
#             self.model.objects.create(basic_info=self.request.user)
#         return super().get(request)

#     def get_object(self, queryset=None):
#         obj = self.model.objects.get(basic_info=self.request.user)
#         return obj

#     def form_valid(self, form):
#         """If the form is valid, save the associated model."""
#         print(self.request.FILES)
#         # dp = self.request.FILES["dp"]
#         # back_dp = self.request.FILES["background_dp"]
#         # fs = FileSystemStorage()
#         # fs.save(dp.name, dp)
#         # fs.save(back_dp.name, back_dp)
#         self.object = form.save()
#         return super().form_valid(form)


def user_profile_edit_view(request):
    try:
        profile = UserProfile.objects.get(basic_info=request.user)
    except:
        profile = UserProfile.objects.create(basic_info=request.user)
        profile.save()
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        files = request.FILES
        posts = request.POST
        print(files)
        if form.is_valid():
            form.save()
            return redirect("profile:profile")
    form = UserProfileForm(instance=profile)
    return render(request, "profiles/edit_profile.html", {"form": form})


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
    template_name = "profiles/edit_profile.html"
    form_class = UserInfoForm
    model = User
    success_url = reverse_lazy("profile:profile")

    def get_object(self, queryset=None):
        pk = self.request.user.id
        queryset = self.model.objects.all()
        obj = queryset.get(pk=pk)
        return obj
