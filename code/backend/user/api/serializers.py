from rest_framework import serializers
from user.models import User, MyCourses


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # will include all fields in model


class MyCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCourses
        fields = "__all__"  # will include all fields in model
