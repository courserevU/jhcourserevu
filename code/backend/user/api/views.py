from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from course.api.serializers import CourseSerializer
from course.models import Course
from user.models import MyCourses, CustomUser
from django.contrib.auth.models import User
from .serializers import CustomUserSerializer, MyCoursesSerializer, AuthUserSerializer
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.pagination import PageNumberPagination


class UserDetail(APIView):
    def get(self, request, user_id, format=None):
        """
        Get users' courses by user's id
        """
        user_id = self.kwargs["user_id"]
        print(user_id)
        user_courses = MyCourses.objects.filter(user_id=user_id)
        s = MyCoursesSerializer(user_courses, many=True)

        if not s.data:
            return Response(status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        courses = Course.objects.filter(id__in=s.data[0]["courses"])
        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)


class UserByEmail(APIView):
    def get(self, request, user_email, format=None):
        email = self.kwargs["user_email"]
        if email is not None:
            user = CustomUser.objects.filter(email=email).first()
            if user is not None:
                return Response({"id": user.id}, status=status.HTTP_200_OK)
                # serializer = AuthUserSerializer(user)
                # serializer = CustomUserSerializer(user)
                # return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(APIView):
    def post(self, request, *args, **kwargs):
        """
        Add course to user's set of "my courses"
        """
        data = {
            "user": request.data.get("user_id"),
            "courses": [request.data.get("course_id")],
        }

        serializer = MyCoursesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, format=None):
    #     """
    #     Get users' courses by user's id
    #     """
    #     user_id = request.data.get("user_id")
    #     # user = CustomUser.objects.filter(user_id=user_id).first()
    #     # if user is None:
    #     #     return Response(status=status.HTTP_404_NOT_FOUND)
    #     # else:
    #     #     serializer = CustomUserSerializer(user)
    #     #     return Response(serializer.data)
    #     user_courses = MyCourses.objects.filter(user_id=user_id)
    #     s = MyCoursesSerializer(user_courses, many=True)

    #     if not s.data:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     paginator = PageNumberPagination()
    #     paginator.page_size = 10
    #     courses = Course.objects.filter(id__in=s.data[0]["courses"])
    #     result_page = paginator.paginate_queryset(courses, request)
    #     serializer = CourseSerializer(result_page, many=True)

    #     return paginator.get_paginated_response(serializer.data)

    def delete(self, request, format=None):
        """
        Delete a course in user's set of courses
        """
        user_id = request.data.get("user_id")
        course_id = request.data.get("course_id")

        user_courses = MyCourses.objects.filter(user_id=user_id)
        s = MyCoursesSerializer(user_courses, many=True)

        if not s.data:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if course_id in s.data[0]["courses"]:
            s.data[0]["courses"].remove(course_id)
            s.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_404_NOT_FOUND)
