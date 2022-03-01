# from socketserver import StreamRequestHandler
# from typing_extensions import Self
# from students.models import Student
from django.db import models


class Semester(models.Model):
    """
    Represents a semester which is composed of a name (e.g. Spring, Fall)
    and a year (e.g. 2022).
    Attributes:
        name (CharField): the name (e.g. Spring, Fall)
        year (CharField): the year (e.g. 2022, 2023)
    """

    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)

    def __unicode__(self):
        return "{} {}".format(self.name, self.year)

    def __str__(self):
        return "{} {}".format(self.name, self.year)


class Course(models.Model):
    """
    TODO: add comments
    """

    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    code = models.CharField(max_length=20)
    num_credits = models.FloatField(default=-1)
    department = models.CharField(max_length=255, default="", null=True)
    level = models.CharField(max_length=500, default="", null=True)
    prerequisites = models.TextField(default="", null=True)
    corequisites = models.TextField(default="", null=True)
    school = models.CharField(db_index=True, max_length=100)
    campus = models.CharField(max_length=300, default="")
    notes = models.TextField(default="", null=True)
    info = models.TextField(default="", null=True)
    unstopped_description = models.TextField(default="")
    exclusions = models.TextField(default="")
    instructors = models.CharField(max_length=500, default="TBA")

    # def view_course():
    #     return "%s, %s" % (Self.name, Self.number)
    # return course description summary


"""
TODO: add comments

"""


class Review(models.Model):
    """
    TODO: add comments
    Each course has multiple reviews
    """

    content = models.CharField(max_length=350, default="-")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_updated = models.DateTimeField(auto_now_add=True)

    # def author(self):
    # anonymize
    #    return Student.objects.get(user=self.user).name
    # COURSES_CHOICES = Student.objects.get(user=self.user).courses

    # def add_review(rev):
    #     return
