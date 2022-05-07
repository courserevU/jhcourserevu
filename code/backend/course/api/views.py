from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


from course.models import Course, Review, Comment
from .serializers import CourseSerializer, ReviewSerializer, CommentSerializer

from django.http import Http404
from rest_framework.pagination import PageNumberPagination


class CourseList(APIView):
    def get(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10
        courses = Course.objects.all()
        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class QueryByNameCourseList(APIView):
    def get(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10

        query = self.request.GET.get("q")
        courses = Course.objects.filter(name__icontains=query)

        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class QueryByNumberCourseList(APIView):
    def get(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10

        query = self.request.GET.get("q")
        courses = Course.objects.filter(course_num__icontains=query)

        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class QueryByDepartmentCourseList(APIView):
    def get(self, request, *args, **kwargs):
        paginator = PageNumberPagination()
        paginator.page_size = 10

        query = self.request.GET.get("q")
        courses = Course.objects.filter(department__icontains=query)

        result_page = paginator.paginate_queryset(courses, request)
        serializer = CourseSerializer(result_page, many=True)
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


class CommentList(APIView):
    def get(self, request, *args, **kwargs):
        """
        List of all possible comments
        """
        paginator = PageNumberPagination()
        paginator.page_size = 10
        comments = Comment.objects.all()
        result_page = paginator.paginate_queryset(comments, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Create review associated with given course
        """
        comments = []
        data = {
            "course": request.data.get("course_id"),
        }
        review_serializer = ReviewSerializer(data=data)
        if review_serializer.is_valid():
            review_serializer.save()
        else:
            return Response(
                review_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        comments_data = request.data.get("comments")
        for category, comment in comments_data.items():
            if not (comment and not comment.isspace()):
                continue

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

        return Response(comments, status=status.HTTP_201_CREATED)


class ReviewByCommentList(APIView):
    def get(self, request, course_id, comment_label, format=None):
        """
        Get Teach Style comments by course id
        """
        paginator = PageNumberPagination()
        paginator.page_size = 10

        comments_to_display = []

        course_id = self.kwargs["course_id"]
        comment_label = self.kwargs["comment_label"]
        reviews = Review.objects.filter(course=course_id)

        for review in reviews:
            comments = review.comment_set.all()

            for comment in comments:
                if comment.category == comment_label:
                    print(comment.comment)
                    serializer = CommentSerializer(comment)
                    comments_to_display.append(serializer.data)

        result_page = paginator.paginate_queryset(comments_to_display, request)
        return paginator.get_paginated_response(result_page)


class ReviewIdList(APIView):
    def get(self, request, course_id, format=None):
        """
        Get review by course id
        """
        paginator = PageNumberPagination()
        paginator.page_size = 10

        reviews_to_display = []

        course_id = self.kwargs["course_id"]
        reviews = Review.objects.filter(course=course_id)

        for review in reviews:
            review_comments = []
            comments = Comment.objects.filter(review=review.id)
            for comment in comments:
                serializer = CommentSerializer(comment)
                review_comments.append(serializer.data)

            reviews_to_display.append(review_comments)

        result_page = paginator.paginate_queryset(reviews_to_display, request)
        return paginator.get_paginated_response(result_page)

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

    def delete(self, request, course_id, format=None):
        """
        Delete review by id
        NOTE: course_id is actually the review id in this case
        """
        review_id = self.kwargs["course_id"]

        review = Review.objects.get(id=review_id)
        review.delete()

        comments = Comment.objects.filter(review=review.id)
        for comment in comments:
            comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
