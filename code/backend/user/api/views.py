from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from .serializers import UserSerializer

from django.contrib.sites.shortcuts import get_current_site


class UserDetail(APIView):
    def get(self, request, *args, **kwargs):
        """
        Get users' courses by user's id
        """
        user_id = self.kwargs["user_id"]
        curr_user = User.objects.filter(user=user_id)

        curr_user_courses = []
        for course in curr_user:
            curr_user_courses.append(course.course)
            
        
        return Response(curr_user_courses)

    def post(self, request, *args, **kwargs):
        """
        Add user courses' to "my courses"
        """
        data = {
            "course": request.data.get("course_id"),
        }

        serializer = UserSerializer(data=data)
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
