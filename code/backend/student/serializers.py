from models import User
from rest_framework import serializers
from student.models import User


class UserSerializer(serializers.ModelSerializer):

    jhed_id = serializers.CharField(required=True, allow_blank=False, max_length=50)
    jhed_email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    preferred_name = serializers.CharField(required=False, allow_blank=True, max_length=30)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.jhed_id = validated_data.get('jhed_id', instance.jhed_id)
        instance.jhed_email = validated_data.get('jhed_email', instance.jhed_email)
        instance.preferred_name = validated_data.get('preferred_name', instance.preferred_name)
        instance.save()
        return instance