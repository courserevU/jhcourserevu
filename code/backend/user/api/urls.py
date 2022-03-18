# from django.conf.urls import url
from django.urls import path
from .views import UserListApiView

urlpatterns = [
    path("", UserListApiView.as_view()),
]
