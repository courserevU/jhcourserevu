from models import Student
from rest_framework import serializers
from student.models import User, Student, Administrator


class UserSerializer(serializers.ModelSerializer):
    student = serializers.RelatedField(many=False)

    jhed_id = serializers.CharField(required=True, allow_blank=False, max_length=50)
    jhed_email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
    preferred_name = serializers.CharField(required=False, allow_blank=True, max_length=30)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.jhed_id = validated_data.get('jhed_id', instance.jhed_id)
        instance.jhed_email = validated_data.get('jhed_email', instance.jhed_email)
        instance.preferred_name = validated_data.get('preferred_name', instance.preferred_name)
        instance.save()
        return instance

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=50)

    def create(self, validated_data):
        """
        Create and return a new `Student` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Student` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

class AdministratorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Administrator` instance, given the validated data.
        """
        return Administrator.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Student` instance, given the validated data.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance