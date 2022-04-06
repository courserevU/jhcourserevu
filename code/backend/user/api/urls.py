# from django.conf.urls import url
from django.urls import path
from .views import UserList

urlpatterns = [
    path("", UserList.as_view()),
]
