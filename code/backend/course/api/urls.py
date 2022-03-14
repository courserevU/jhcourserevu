from django.urls import path
from .views import CourseListApiView

urlpatterns = [
    path("", CourseListApiView.as_view()),
]