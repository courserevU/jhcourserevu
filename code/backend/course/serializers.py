from models import Course, Review
from rest_framework import serializers
from course.models import Course, LANGUAGE_CHOICES, STYLE_CHOICES, Review

class CourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    course_num = serializers.CharField(required=False, allow_blank=True, max_length=20)
    num_credits = serializers.FloatField(max_value=15.0, min_value=-1)
    department = serializers.CharField(required=False, allow_blank=True, max_length=255)
    level = serializers.CharField(required=False, allow_blank=True, max_length=500)
    prerequisites = serializers.CharField(style={'base_template': 'textarea.html'})
    corequisites = serializers.CharField(style={'base_template': 'textarea.html'})
    school = serializers.CharField(required=False, allow_blank=True, max_length=100)
    campus = serializers.CharField(required=False, allow_blank=True, max_length=300)
    notes = serializers.CharField(style={'base_template': 'textarea.html'})
    info = serializers.CharField(style={'base_template': 'textarea.html'})
    exclusions = serializers.CharField(style={'base_template': 'textarea.html'})
    instructors = serializers.CharField(required=False, allow_blank=True, max_length=500)
    
    # faculty = serializers.ManyToManyField(models.faculty)
    # semester = serializers.CharField(required=False, allow_blank=True, max_length=20)
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
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.course_num = validated_data.get('course_num', instance.number)
        instance.num_credits = validated_data.get('num_credits', instance.num_credits)
        instance.department = validated_data.get('department', instance.department)
        instance.level = validated_data.get('level', instance.level)
        instance.prerequisites = validated_data.get('prerequisites', instance.prerequisites)
        instance.corequisites = validated_data.get('corequisites', instance.corequisites)
        instance.school = validated_data.get('school', instance.school)
        instance.campus = validated_data.get('campus', instance.campus)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.info = validated_data.get('info', instance.info)
        instance.exclusions = validated_data.get('exclusions', instance.exclusions)
        instance.instructors = validated_data.get('instructors', instance.instructors)
        # instance.semester = validated_data.get('semester', instance.semester)
        
        instance.save()
        return instance

class ReviewSerializer(serializers.ModelSerializer):
    course = serializers.CharField(required=False, allow_blank=True, max_length=255)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    time_posted = serializers.DateTimeField(required=False, allow_blank=True)

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.course = validated_data.get('course', instance.course)
        instance.content = validated_data.get('content', instance.content)
