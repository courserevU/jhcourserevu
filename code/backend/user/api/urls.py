from django.urls import path, re_path
from .views import UserUpdate, UserByEmail

urlpatterns = [
    path("", UserUpdate.as_view(), name="user_update"),
    path("get_by_email", UserByEmail.as_view(), name="user_get_id"),
]
