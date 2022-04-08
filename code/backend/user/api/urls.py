# from django.conf.urls import url
from django.urls import path
from .views import UserList

urlpatterns = [
    path("", UserList.as_view()),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft'))
]
