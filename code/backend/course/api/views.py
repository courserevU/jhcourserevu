from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from course.models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer

from django.http import Http404, HttpResponse
import json
from django.forms import model_to_dict
from django.core.paginator import Paginator

# from rest_framework import permissions
# from django.shortcuts import render


class CourseList(APIView):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        courses_per_page = 50
        paginator = Paginator(courses, courses_per_page)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        courses_list = []

        for course in courses:
            course_dict = model_to_dict(course)
            courses_list.append(course_dict)

        json_data = {"courses": courses_list}
        return HttpResponse(json.dumps(json_data), content_type="application/json")
        # return render(request, 'all_courses.html', {'page_obj': page_obj})


class CourseNumber(APIView):
    """
    Get course by course number
    """

    def get_object(self, course_num):
        try:
            return Course.objects.get(course_num=course_num)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, course_num, format=None):
        """
        Get course by course number
        """
        c_n = self.get_object(course_num)
        serializer = CourseSerializer(c_n)
        return Response(serializer.data)


class ReviewList(APIView):
    def get(self, request, *args, **kwargs):
        """
        List of all reviews
        """
        reviews = Review.objects.all()
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


class ReviewDetail(APIView):
    def get(self, request, pk, format=None):
        """
        Get review by id
        """
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        Update review by id
        """
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete review by id
        """
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def get_reviews_by_course(request, course):
#     reviews = Review.objects.get(course=course)
#     review_list = []
#     for review in reviews:
#         review_dict = model_to_dict(review)
#         review_list.append(review_dict)
#     json_data = {"reviews": review_list}
#     return HttpResponse(json.dumps(json_data), content_type="application/json")
