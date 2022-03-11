from models import Course
from rest_framework import serializers
from course.models import Course, LANGUAGE_CHOICES, STYLE_CHOICES

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 
                  'description', 
                  'number', 
                  'num_credits', 
                  'department', 
                  'level', 
                  'prerequisites',
                  'corequisites',
                  'school',
                  'campus',
                  'notes',
                  'info',
                  'exclusions',
                  'instructors']