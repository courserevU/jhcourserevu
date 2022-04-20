from django.urls import path, re_path
from course.api.views import CourseList, CommentList, CourseNumberList, ReviewIdList

from . import views

urlpatterns = [
    path('api/', CourseList.as_view(), name='course_api'),
    re_path('^api/(?P<course_num>.+)/$', CourseNumberList.as_view(), name='course_num_api'),
    path('review/api/', CommentList.as_view(), name='comment_api'),
    re_path('^review/api/(?P<course_id>.+)/$', ReviewIdList.as_view(), name='comments_by_course_api'),
]
