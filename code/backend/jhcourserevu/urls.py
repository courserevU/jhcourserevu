"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
# from user.api.views import GoogleLogin

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # path("accounts/", include("allauth.urls")),
    # path("dj-rest-auth/", include("dj_rest_auth.urls")),
    # path("dj-rest-auth/google/", GoogleLogin.as_view(), name="google_login"),
    # path("api-auth/", include("rest_framework.urls")),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path("course/", include("course.urls"), name="course"),
    path("user/", include("user.urls"), name="user"),
]
