from django.urls import path, re_path
from .views import UserUpdate, UserDetail

urlpatterns = [
    path("", UserUpdate.as_view(), name="user_update"),
]
