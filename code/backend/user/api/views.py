from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from course.api.serializers import CourseSerializer
from course.models import Course

from user.models import User, MyCourses
from .serializers import UserSerializer, MyCoursesSerializer

from django.contrib.sites.shortcuts import get_current_site
from rest_framework.pagination import PageNumberPagination

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# from allauth.socialaccount.providers.oauth2.client import OAuth2Client

# if you want to use Authorization Code Grant, use this
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
#     client_class = OAuth2Client

# if you want to use Implicit Grant, use this
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


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
        courses = Course.objects.filter(id__in=s.data[0]["courses"])
        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

        # TODO: no pagination, may remove
        # courses = Course.objects.filter(id__in=s.data[0]["courses"])
        # serializer = CourseSerializer(courses, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, user_id, format=None):
        """
        Delete a course in user's set of courses
        """
        user_id = self.kwargs["user_id"]
        course_id = request.data.get("course_id")

        user_courses = MyCourses.objects.filter(user=user_id)
        s = MyCoursesSerializer(user_courses, many=True)

        if not s.data:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if course_id in s.data[0]["courses"]:
            s.data[0]["courses"].remove(course_id)
            s.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_404_NOT_FOUND)


def test_sso_view(request):
    current_site = get_current_site(request)
    if current_site.domain == "login.microsoftonline.com":
        pass
    else:
        pass
