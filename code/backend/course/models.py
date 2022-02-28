from socketserver import StreamRequestHandler
from typing_extensions import Self
from django.db import models

# Create your models here.

class Course(models.Model): 
    number = models.CharField(max_length = 20)
    name = models.CharField(max_length = 30)
    faculty = models.ManyToManyField(models.faculty)
    semester = models.CharField(max_length = 20)
    description = models.TextField()
    pre_reqs = models.ManyToManyField(models.course)
    # reviews = models.ForeignKey(models.review)

    def edit_course():
        return

    # def add_review(rev):
    #     return

    def view_course():
        return "%s, %s" % (Self.name, Self.number)
        # return course description summary    


