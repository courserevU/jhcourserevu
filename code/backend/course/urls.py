from django.urls import path, include
from course.api.views import CourseList, ReviewList, CourseNumber

from . import views

urlpatterns = [
    path('api/', CourseList.as_view(), name='course_api'),
    # path('api/<string: course_num>', CourseList.as_view(), name='course_api'),
    path('review/api/', ReviewList.as_view(), name='review_api'),
]
