from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from course.api.serializers import CourseSerializer
from course.models import Course

from user.models import User, MyCourses
from .serializers import UserSerializer, MyCoursesSerializer

from django.contrib.sites.shortcuts import get_current_site


class UserDetail(APIView):
    def get(self, request, user_id, format=None):
        """
        Get users' courses by user's id
        """
        user_id = self.kwargs["user_id"]
        user_courses = MyCourses.objects.filter(user=user_id)

        courses = []
        for course in user_courses:
            c = Course.objects.filter(course=course.course_id)
            serializer = CourseSerializer(c)
            courses.append(serializer.data)
        
        return Response(courses, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Add course to user's set of "my courses"
        """
        data = {
            "course": request.data.get("course_id"),
        }

        serializer = MyCoursesSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def test_sso_view(request):
    current_site = get_current_site(request)
    if current_site.domain == "login.microsoftonline.com":
        pass
    else:
        pass
