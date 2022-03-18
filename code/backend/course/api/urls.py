from django.urls import path
from .views import CourseListApiView, ReviewListApiView

urlpatterns = [
    path("", CourseListApiView.as_view()),
    # path("", ReviewListApiView.as_view()),
    # path('api/write_review/', views.write, name='write'),
    # path('api/read/', views.read, name='read'),
    # path('api/browse/', views.browse, name='browse'),
    # path('api/login/', views.login, name='login'),
    # path('api/dashboard/', views.dashboard, name='dashboard'),
]