from django.db import models
from django.contrib.auth.models import User
from course.models import Course
from django.contrib.sites.models import Site


class User(models.Model):
    """
    Represents any user with required JHED email. This is necessary to log into
    the main website and access
    Attributes:
        user (:obj:`OneToOneField`): inherits Django user basic settings
        jhed_id (:obj:`CharField`): Hopkins affiliate's JHED ID
        jhed_email (:obj:`EmailField`): Hopkins affiliate's University Email
        preferred_name (:obj:`CharField`): user's preferred name
        is_admin (:obj:`BooleanField`): indicates whether user is a moderator or visiting user
    """

    user = models.OneToOneField(User, on_delete=models.deletion.CASCADE)
    jhed_id = models.CharField(max_length=50, blank=True, null=True, unique=True)
    jhed_email = models.EmailField(("email address"), unique=True)
    class_year = models.CharField(max_length=50, blank=True, null=True, unique=True)
    preferred_name = models.CharField(max_length=30, blank=True, null=True, unique=True)
    is_admin = models.BooleanField(null=False)


class MyCourses(models.Model):
    """
    The set of courses a user is enrolled in
    Attributes:
    user (:obj:`ForeignKey`): user associated with set of courses
    courses(:obj:`ForeignKey`): courses that the user is enrolled in
    """

    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE)
    courses = models.ManyToManyField(Course)

    def get_courses(self):
        return self.courses.all()
