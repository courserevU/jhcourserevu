from django.shortcuts import render

# Create your views here. (The following is copy pasted from https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is a JHU course review page.")
