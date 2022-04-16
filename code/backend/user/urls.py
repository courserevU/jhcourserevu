from django.urls import path, include, re_path
from user.api.views import UserDetail

urlpatterns = [
    path("api/", include("user.api.urls")),
    re_path('^api/(?P<user_id>.+)/$', UserDetail.as_view(), name='courses_by_user'),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft'))
]
