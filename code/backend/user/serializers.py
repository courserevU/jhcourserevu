from rest_framework import serializers

from models import User
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    userFirstName = serializers.CharField(source="user.first_name")
    userLastName = serializers.CharField(source="user.last_name")
    class Meta:
        model = User
        fields = ['jhed_id', 'jhed_email', 'class_year', 'preferred_name', 'userFirstName', 'userLastName']
    
        def create(self, validated_data):
            """
            Create and return a new `User` instance, given the validated data.
            """
            return User.objects.create(**validated_data)
