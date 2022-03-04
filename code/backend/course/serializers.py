from models import Course
from rest_framework import serializers
from course.models import Course, LANGUAGE_CHOICES, STYLE_CHOICES

class CourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=255)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    number = serializers.CharField(required=False, allow_blank=True, max_length=20)
    num_credits = serializers.FloatField(max_value=15.0, min_value=-1)
    department = serializers.CharField(required=False, allow_blank=True, max_length=255)
    level = serializers.CharField(required=False, allow_blank=True, max_length=500)
    # prerequisites = serializers.TextField
    
    # faculty = serializers.ManyToManyField(models.faculty)
    semester = serializers.CharField(required=False, allow_blank=True, max_length=20)
    
    # pre_reqs = serializers.ManyToManyField(models.course)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.number = validated_data.get('number', instance.number)
        instance.name = validated_data.get('name', instance.name)
        instance.faculty = validated_data.get('faculty', instance.faculty)
        instance.semester = validated_data.get('semester', instance.semester)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance