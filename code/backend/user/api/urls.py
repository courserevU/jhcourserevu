from django.urls import path, re_path
from .views import UserUpdate, UserDetail, GoogleLogin

urlpatterns = [
    path("", UserUpdate.as_view(), name="user_update"),
    # path('rest-auth/google/', GoogleLogin.as_view(), name='redirect'),
    re_path("(?P<user_id>.+)/$", UserDetail.as_view(), name="courses_by_user"),
]
