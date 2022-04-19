from django.urls import path, include

urlpatterns = [
    path("api/", include("user.api.urls")),
    # path('accounts/', include('allauth.urls')),
    # path("microsoft/", include("microsoft_auth.urls", namespace="microsoft")),
]
