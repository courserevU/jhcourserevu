from django.contrib import admin
from .models import MyCourses, CustomUser

admin.site.register(CustomUser)
admin.site.register(MyCourses)
