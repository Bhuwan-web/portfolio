from email.policy import default
from statistics import mode
from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
# Create your models here.
class UserProfile(models.Model):

    basic_info = models.OneToOneField(User, verbose_name=_(""), on_delete=models.CASCADE)
    dp = models.ImageField(_("Profile Pic"), blank=True, null=True, upload_to="dp")
    bio = models.CharField(_("Bio"), max_length=50)
    background_dp = models.ImageField(_("Background Pic"), blank=True, null=True, upload_to="back_dp")
    role = models.CharField(_("Role that best justifies you"), max_length=50, null=True)
    tech1 = models.ImageField(_("Technology 1"), max_length=150, upload_to="tech", null=True)
    tech2 = models.ImageField(_("Technology 2"), max_length=150, upload_to="tech", null=True)
