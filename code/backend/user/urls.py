from django.urls import path, include

urlpatterns = [
    path("api/", include("user.api.urls")),
    path("microsoft/", include("microsoft_auth.urls", namespace="microsoft")),
]
