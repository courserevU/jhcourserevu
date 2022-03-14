from django.urls import path, include

# from django.contrib import admin
# from django.conf.urls import include
# from . import views

urlpatterns = [
    path("api/", include("user.api.urls")),
    # path('auth/', include('rest_auth.urls')),
]
