from django.urls import path, re_path
from course.api.views import CourseList, CommentList, CourseNumberList, QueryByNameCourseList, QueryByNumberCourseList, QueryByDepartmentCourseList

urlpatterns = [
    path('api/', CourseList.as_view(), name='course_api'),
    re_path('^api/(?P<course_num>.+)/$', CourseNumberList.as_view(), name='course_num_api'),
    path('review/api/', CommentList.as_view(), name='comment_api'),
    path("search/name/", QueryByNameCourseList.as_view(), name="search_by_name"),
    path("search/course_num/", QueryByNumberCourseList.as_view(), name="search_by_number"),
    path("search/department/", QueryByDepartmentCourseList.as_view(), name="search_by_number"),
]
