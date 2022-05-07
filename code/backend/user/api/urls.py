from django.urls import path, re_path
from .views import UserUpdate, UserByEmail, UserDetail

urlpatterns = [
    path("", UserUpdate.as_view(), name="user_update"),
    re_path("^id/(?P<user_id>.+)/$", UserDetail.as_view(), name="user_detail"),
    re_path("^(?P<user_email>.+)/$", UserByEmail.as_view(), name="user_get_id"),
]
