from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework import permissions
from course.models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer


class CourseListApiView(APIView):
    def get(self, request, *args, **kwargs):
        """
        List all courses
        """
        # TODO: get section_type from request?
        courses = Course.objects.filter(course_num=request.data.course_num)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create new course
        """
        data = {
            "name": request.data.get("name"),
            "description": request.data.get("description"),
            "course_num": request.data.get("course_num"),
            "num_credits": request.data.get("num_credits"),
            "department": request.data.get("department"),
            "level": request.data.get("level"),
            "prerequisites": request.data.get("prerequisites"),
            "corequisites": request.data.get("corequisites"),
            "school": request.data.get("school"),
            "campus": request.data.get("campus"),
            "is_writing_intensive": request.data.get("is_writing_intensive"),
            "meeting_section": request.data.get("meeting_section"),
            "size": request.data.get("size"),
            "enrollment": request.data.get("enrollment"),
            "waitlist": request.data.get("waitlist"),
            "instructors": request.data.get("instructors"),
            "semester": request.data.get("semester"),
            "is_full": request.data.get("is_full"),
        }

        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewListApiView(APIView):
    def get(self, request, *args, **kwargs):
        """
        List of all reviews
        """
        # TODO: get by id or by course_num???
        reviews = Review.objects.filter(review_id=request.data.review_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        """
        List of all reviews for given course
        """
        # TODO: get by course_id
        reviews = Review.objects.filter(course_id=request.data.course_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create review associated with given course
        """
        data = {
            "comments": request.data.get("comments"),
            "course_id": request.data.get("course_id"),
            "course_section_id": request.data.get("course_section_id"),
        }

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
