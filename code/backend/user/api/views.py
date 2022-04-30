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
from django.db.models import Q


class UserDetail(APIView):
    def get(self, request, user_id, format=None):
        """
        Get users' courses by user's id
        """
        user_id = self.kwargs["user_id"]
        user_courses = MyCourses.objects.filter(user=user_id)
        s = MyCoursesSerializer(user_courses, many=True)

        if not s.data:
            return Response(status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        courses = Course.objects.none()
        for dictionary in s.data:
            courses = courses | Course.objects.filter(id=dictionary.get("courses")[0])
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
        # user_courses = MyCourses.objects.filter(user=(request.data.get("user_id"))).first()
        # data = {}

        data = {
            "user": request.data.get("user_id"),
            "courses": [request.data.get("course_id")],
        }
        serializer = MyCoursesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # NOTE: Commented out code below was unnecessary but may still be useful to combine
        #       all of a user's courses into one object (not having multiple MyCourses for one user)
        # No existing MyCourses for this user
        # if user_courses is None:
        #     data = {
        #         "user": request.data.get("user_id"),
        #         "courses": [request.data.get("course_id")],
        #     }
        #     serializer = MyCoursesSerializer(data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # # This user already has an associated MyCourses, append new course
        # else:
        #     course_list = list(getattr(user_courses, "courses").all())
        #     course_list.append(request.data.get("course_id"))
        #     print(course_list)
        #     data = {
        #         "user": request.data.get("user_id"),
        #         "courses": course_list,
        #     }
            
        #     serializer = MyCoursesSerializer(user_courses, data=data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_200_OK)

        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, format=None):
        """
        Delete a course in user's set of courses
        """
        user_id = request.data.get("user_id")
        course_id = request.data.get("course_id")

        MyCourses.objects.filter(Q(user=user_id) & Q(courses=course_id)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
