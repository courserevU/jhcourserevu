import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


from course.models import Course, Review, Comment
from .serializers import CourseSerializer, ReviewSerializer, CommentSerializer

from django.http import Http404, HttpResponse
import json
from django.forms import model_to_dict
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination

# from rest_framework import permissions
# from django.shortcuts import render


class CourseList(APIView):
    def get(self, request, *args, **kwargs):
        # courses = Course.objects.all()
        # courses_per_page = 50
        # paginator = Paginator(courses, courses_per_page)
        # page_number = request.GET.get("page")
        # page_obj = paginator.get_page(page_number)
        # courses_list = []

        # for course in courses:
        #     course_dict = model_to_dict(course)
        #     courses_list.append(course_dict)

        # json_data = {"courses": courses_list}
        # return HttpResponse(json.dumps(json_data), content_type="application/json")
        # return render(request, 'all_courses.html', {'page_obj': page_obj})

        paginator = PageNumberPagination()
        paginator.page_size = 10
        courses = Course.objects.all()
        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(result_page, many=True)  # MAIN CHANGE IS HERE
        return paginator.get_paginated_response(serializer.data)


class CourseNumberList(generics.ListAPIView):
    """
    Get course by course number
    """

    def get_queryset(self):
        c_n = self.kwargs["course_num"]
        try:
            return Course.objects.filter(course_num=c_n)
        except Course.DoesNotExist:
            raise Http404

    """
    Use serializer to return JSON
    """

    def get_serializer_class(self):
        return CourseSerializer

    # def get_object(self, course_num):
    #     try:
    #         return Course.objects.get(course_num=course_num)[0]
    #     except Course.DoesNotExist:
    #         raise Http404

    # def get(self, request, course_num, format=None):
    #     """
    #     Get course by course number
    #     """
    #     c_n = self.get_object(course_num)
    #     serializer = CourseSerializer(c_n)
    #     return Response(serializer.data)


class CommentList(APIView):
    def get(self, request, *args, **kwargs):
        """
        List of all possible reviews and their comments
        """
        paginator = PageNumberPagination()
        paginator.page_size = 10
        reviews = Review.objects.get(course=request.data.get("course_id"))
        result_page = paginator.paginate_queryset(reviews, request)
        serializer = ReviewSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Create review associated with given course
        """
        comments = []

        comments_data = request.data.get("comments")
        for category, comment in comments_data.items():

            data = {
                "review": review_serializer.data.get("id"),
                "comment": comment,
                "category": category,
            }

            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                comments.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Now create the review with the serialized comments
        data = {
            "course": request.data.get("course_id"),
            "comments": comments,
        }
        review_serializer = ReviewSerializer(data=data)
        if review_serializer.is_valid():
            review_serializer.save()
        else:
            return Response(
                review_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(comments, status=status.HTTP_201_CREATED)


class ReviewIdList(APIView):
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
