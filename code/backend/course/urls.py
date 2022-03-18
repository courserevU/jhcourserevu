from django.urls import path, include
from course.api.views import CourseListApiView, ReviewListApiView

from . import views

urlpatterns = [
    path('api/', CourseListApiView.as_view(), name='course_api'),
    path('review/api/', ReviewListApiView.as_view(), name='review_api'),
]
