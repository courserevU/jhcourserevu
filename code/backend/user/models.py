from django.db import models
from django.contrib.auth.models import User

# from django.utils.translation import ugettext_lazy as _

# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date


class User(models.Model):
    """
    TODO: edit
    Attributes:
        user (:obj:`OneToOneField`):
        jhed_id (:obj:`CharField`):
        jhed_email (:obj:`EmailField`):
        preferred_name (:obj:`CharField`):
    """

    user = models.OneToOneField(User, on_delete=models.deletion.CASCADE)
    jhed_id = models.CharField(max_length=50, blank=True, null=True, unique=True)
    jhed_email = models.EmailField(("email address"), unique=True)
    class_year = models.IntegerField(blank=True, null=True)
    preferred_name = models.CharField(max_length=30)

    isAdmin = models.BooleanField(null=False)
