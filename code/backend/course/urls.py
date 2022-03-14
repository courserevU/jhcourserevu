from django.urls import path, include

from . import views

urlpatterns = [
    path('api/', include('course.api.urls')),
    # path('api/write_review/', views.write, name='write'),
    # path('api/read/', views.read, name='read'),
    # path('api/browse/', views.browse, name='browse'),
    # path('api/login/', views.login, name='login'),
    # path('api/dashboard/', views.dashboard, name='dashboard'),
]
