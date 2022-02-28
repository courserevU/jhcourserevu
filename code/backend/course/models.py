from socketserver import StreamRequestHandler
from typing_extensions import Self
from django.db import models
#from students.models import Student

class Course(models.Model): 
    number = models.CharField(max_length = 20)
    name = models.CharField(max_length = 30)
    faculty = models.ManyToManyField(models.faculty)
    semester = models.CharField(max_length = 20)
    description = models.TextField()
    pre_reqs = models.ManyToManyField(models.course)
    # reviews = models.ForeignKey(models.review)

    #     def edit_course():
    #         return

    # def add_review(rev):
    #     return

    def view_course():
        return "%s, %s" % (Self.name, Self.number)
        # return course description summary    

class Review(models.Model):
    #def author(self):
        # anonymize
    #    return Student.objects.get(user=self.user).name

    #COURSES_CHOICES = Student.objects.get(user=self.user).courses

    review_content = models.CharField(max_length=350, default='-')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now_add=True)
