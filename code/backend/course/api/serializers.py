from rest_framework import serializers
from course.models import Course, Review, Comment


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
        instance.content = validated_data.get("comments", instance.comments)
        #instance.work = validated_data.get("work", instance.work)
        #instance.workload = validated_data.get('workload', instance.workload)
        #instance.assignment_style = validated_data.get('assignment_style', instance.assignment_style)
        #instance.exam_style = validated_data.get('exam_style', instance.exam_style)
        #instance.outside_time = validated_data.get('outside_time', instance.outside_time)
        #instance.teaching_style = validated_data.get('teaching_style', instance.teaching_style)
        #instance.teaching_effectiveness = validated_data.get('teaching_effectiveness', instance.teaching_effectiveness)
        #instance.prof_availability = validated_data.get('prof_availability', instance.prof_availability)
        #instance.grading_style = validated_data.get('grading_style', instance.grading_style)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"  # will include all fields in model
