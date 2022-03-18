from rest_framework import serializers
from course.models import Course, Review


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"  # will include all fields in model


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and return a new `Review` instance, given the validated data.
        """
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return a new `Review` instance, given the validated data.
        """
        instance.course = validated_data.get("course", instance.course)
        instance.content = validated_data.get("content", instance.comments)
