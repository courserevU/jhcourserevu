from django.urls import path
from django.contrib import admin
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', include('rest_auth.urls')),
]
