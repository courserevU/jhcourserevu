from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import CustomUser, MyCourses


class MyCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourses
        fields = "__all__"  # will include all fields in model
