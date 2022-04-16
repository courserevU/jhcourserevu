from django.urls import path, include, re_path
from user.api.views import UserDetail

urlpatterns = [
    path("api/", include("user.api.urls")),
    path("microsoft/", include("microsoft_auth.urls", namespace="microsoft")),
]
