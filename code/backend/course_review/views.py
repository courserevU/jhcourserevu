from django.shortcuts import render

# Create your views here. (The following is copy pasted from https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. This is a JHU course review page.")

def write(request):
    return HttpResponse("Page for writing a review.")

def read(request):
    return HttpResponse("Page for reading a review.")

def browse(request):
    return HttpResponse("Page for viewing all reviews.")

def login(request):
    return HttpResponse("Page for logging a user in.")

def dashboard(request):
    return HttpResponse("Page for a moderator to view a dashboard.")
