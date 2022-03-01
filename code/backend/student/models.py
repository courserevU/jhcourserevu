from django.db import models

# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.models import User, AbstractUser

# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date


class User(models.Model):
    """
    TODO: add comments
    """

    user = models.OneToOneField(User, on_delete=models.deletion.CASCADE)
    jhed_id = models.CharField(max_length=50, blank=True, null=True, unique=True)
    jhed_email = models.EmailField(_("email address"), unique=True)
    preferred_name = models.CharField(max_length=30)


class Administrator(models.Model):
    """
    TODO: add comments
    """

    user = models.OneToOneField(AbstractUser, on_delete=models.deletion.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)


class Student(models.Model):
    """
    TODO: add comments
    """

    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
