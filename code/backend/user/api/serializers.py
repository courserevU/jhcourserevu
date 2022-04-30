from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import CustomUser, MyCourses


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"  # will include all fields in model


class MyCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourses
        fields = "__all__"  # will include all fields in model

    # TODO: fix to access correct table for POST request
    # https://stackoverflow.com/questions/17256724/include-intermediary-through-model-in-responses-in-django-rest-framework/45834689#45834689
    # https://stackoverflow.com/questions/52295480/serializing-many-to-many-intermediate-table-in-django-rest-framework
