from django.views.generic import TemplateView

# Create your views here.
class ProfileView(TemplateView):
    template_name = "home/home.html"
