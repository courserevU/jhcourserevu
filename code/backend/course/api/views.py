from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from course.models import Course
from .serializers import CourseSerializer, ReviewSerializer


class CourseListApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        # TODO: this is incorrect, should get by exact matching
        courses = Course.objects.filter(course_num=request.user.id)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create user within given info
        """
        data = {
            "name": request.data.get("name"),
            # "jhed_id": request.data.get("jhed_id"),
            # "jhed_email": request.data.get("jhed_email"),
            # "class_year": request.data.get("class_year"),
            # "preferred_name": request.data.get("preferred_name"),
            # "is_admin": request.data.get("is_admin"),
        }

        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewListApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all the todo items for given requested user
        """
        # TODO: this is incorrect, should get by exact matching
        reviews = Course.objects.filter(course_num=request.user.id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create user within given info
        """
        data = {
            "name": request.data.get("name"),
            # "jhed_id": request.data.get("jhed_id"),
            # "jhed_email": request.data.get("jhed_email"),
            # "class_year": request.data.get("class_year"),
            # "preferred_name": request.data.get("preferred_name"),
            # "is_admin": request.data.get("is_admin"),
        }

        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)