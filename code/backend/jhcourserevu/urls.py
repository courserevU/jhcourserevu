from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    re_path(r"^auth/", include("drf_social_oauth2.urls", namespace="drf")),
    path("course/", include("course.urls"), name="course"),
    path("user/", include("user.urls"), name="user"),
]
