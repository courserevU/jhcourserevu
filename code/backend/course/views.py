# TODO: delete
# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from course.models import Course
# from course.serializers import CourseSerializer

# Create your views here. (The following is copy pasted from https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
from django.http import HttpResponse
from course.models import Course
from course.models import Review
from course.api.serializers import CourseSerializer
from course.api.serializers import ReviewSerializer

import json
from django.forms import model_to_dict

def get_reviews_by_course(request, course):
    reviews = (Review.objects.get(course=course))
    review_list = []
    for review in reviews:
        review_dict = model_to_dict(review)
        review_list.append(review_dict)
    json_data = {'reviews': review_list}
    return HttpResponse(json.dumps(json_data), content_type='application/json')




# def home(request):
#     return HttpResponse("Hello, world. This is a JHU course review page.")

# def write(request):
#     return HttpResponse("Page for writing a review.")

# def read(request):
#     return HttpResponse("Page for reading a review.")

# def browse(request):
#     return HttpResponse("Page for viewing all reviews.")

# def login(request):
#     return HttpResponse("Page for logging a user in.")

# def dashboard(request):
#     return HttpResponse("Page for a moderator to view a dashboard.")
    