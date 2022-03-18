from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions
from course.models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer


class CourseListApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        List all courses
        """
        # TODO: this is incorrect, should get by exact matching
        courses = Course.objects.filter(course_num=request.user.id)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create new course
        """
        data = {
            "name": request.data.get("name"),
            "course_num": request.data.get("course_num"),
            "description": request.data.get("description"),
            "instructor": request.data.get("instructor"),
            "semester": request.data.get("semester"),
            "year": request.data.get("year"),
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
        List of all reviews
        """
        # TODO: this is incorrect, should get by exact matching
        reviews = Review.objects.filter(course_num=request.course.id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        """
        List of all reviews for given course
        """
        # TODO: should get by exact matching
        reviews = Review.objects.filter(course_num=request.user.id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create review associated with given course
        """
        data = {
            "name": request.data.get("name"),
            "comments": request.data.get("comments"),
            "course_id": request.data.get("course_id"),
            "course_section_id": request.data.get("course_section_id"),
        }

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)