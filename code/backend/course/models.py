from django.db import models
#from students.models import Student

# Create your models here.

class Review(models.Model):
    #def author(self):
        # anonymize
    #    return Student.objects.get(user=self.user).name

    #COURSES_CHOICES = Student.objects.get(user=self.user).courses

    review_content = models.CharField(max_length=350, default='-')
    #course = models.CharField(max_length=50, choices=COURSES_CHOICES, default='-')
    submit_time = models.DateTimeField(auto_now_add=True)