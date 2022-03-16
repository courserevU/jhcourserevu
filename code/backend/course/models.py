# from user.models import User
from django.db import models


class Semester(models.Model):
    """
    Represents a semester which is composed of a name (e.g. Spring, Fall)
    and a year (e.g. 2022).
    Attributes:
        name (:obj:`CharField`): the name (e.g. Spring, Fall)
        year (:obj:`CharField`): the year (e.g. 2022, 2023)
    """

    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)

    def __unicode__(self):
        return "{} {}".format(self.name, self.year)

    def __str__(self):
        return "{} {}".format(self.name, self.year)


class Course(models.Model):
    """
    Represents a university course containing all relevant information, including
    name, description, code, number of credits, department, level, prerequisites,
    corequisities, school, campus, notes, info, exclusions, and instructors.
    Attributes:
        name (:obj:`CharField`): course name (e.g. Intermediate Programming)
        description (:obj:`TextField`): course description (e.g. Learn programming in C++)
        course_num (:obj:`CharField`): course code (e.g. EN.601.421)
        num_credits (:obj:`FloatField`): number of credits hours (e.g. 3 credits)
        department (:obj:`CharField`): department associated with course (e.g. EN)
        level (:obj:`CharField`): course level (e.g. 100, Upper)
        prerequisites (:obj:`TextField`): required courses to complete prior to given course
            (e.g. Gateway Computing: Java)
        corequisites (:obj:`TextField`): required course(s) to complete concurrently
        school (:obj:`CharField`): school associated with course (e.g. Whiting School of Engineering)
        campus (:obj:`CharField`, optional): campus associated with course (e.g. Homewood)
        notes (:obj:`TextField`, optional): notes regarding registration
        info (:obj:`TextField`, optional): additional information about course
        exclusions (:obj:`TextField`, optional): any reasons student may be unable to register for this course
        instructors (:obj:`CharField`): full name of instructors
        is_writing_intensive (:obj:`CharField`): returned as yes/no string
    """

    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    course_num = models.CharField(max_length=20)
    num_credits = models.FloatField(default=-1)
    department = models.CharField(max_length=255, default="", null=True)
    level = models.CharField(max_length=500, default="", null=True)
    prerequisites = models.TextField(default="", null=True)
    corequisites = models.TextField(default="", null=True)
    school = models.CharField(db_index=True, max_length=100)
    campus = models.CharField(max_length=300, default="")
    notes = models.TextField(default="", null=True)
    info = models.TextField(default="", null=True)
    exclusions = models.TextField(default="")
    instructors = models.CharField(max_length=500, default="TBA")
    is_writing_intensive = models.CharField(max_length=10, default="")

    # def view_course():
    #     return "%s, %s" % (Self.name, Self.number)
    # return course description summary


class Section(models.Model):
    """
    TODO: MAYBE scrap, need to look into SIS Web API and see if all data for Section can be found in courses.

    A subset of course. Courses could have one or greater sections and is
    guaranteed to have at least one.

    Attributes:
        course (:obj:`Course`): The course this section belongs to
        course_section_id (:obj:`IntegerField`):
        meeting_section (:obj:`CharField`): the name of the section
            (e.g. 001, L01, LAB2)
        size (:obj:`IntegerField`): the capacity of the course (the enrollment cap)
        enrollment (:obj:`IntegerField`): the number of students registered so far
        waitlist (:obj:`IntegerField`): the number of students waitlisted so far
        waitlist_size (:obj:`IntegerField`): the max size of the waitlist
        section_type (:obj:`CharField`):
            the section type, example 'L' is lecture, 'T' is tutorial, `P` is practical
        instructors (:obj:`CharField`): comma seperated list of instructors
        semester (:obj:`ForeignKey` to :obj:`Semester`): the semester for the section
        was_full (:obj:`BooleanField`): whether the course was full
    """

    course = models.ForeignKey(Course, on_delete=models.deletion.CASCADE)
    course_section_id = models.IntegerField(default=0)
    meeting_section = models.CharField(max_length=50)
    size = models.IntegerField(default=-1)
    enrollment = models.IntegerField(default=-1)
    waitlist = models.IntegerField(default=-1)
    waitlist_size = models.IntegerField(default=-1)
    section_type = models.CharField(max_length=50, default="L")
    instructors = models.CharField(max_length=500, default="TBD")
    semester = models.ForeignKey(Semester, on_delete=models.deletion.CASCADE)
    was_full = models.BooleanField(default=False)

    def is_full(self):
        return self.enrollment >= 0 and self.size >= 0 and self.enrollment >= self.size


class Review(models.Model):
    """
    Represents a single course review's content (e.g. "Great course!")
    associated with a single course (e.g. Data Structures).
    Attributes:
        anon_user (:obj:`ForeignKey`): user associated with review (information not stored)
        comment (:obj:`CharField`): the written review by a user (e.g. "Great course!")
        course (:obj:`ForeignKey`): the course associated with the review (e.g. Data Structures)
        time_update (:obj:`DateTimeField`): the last time user updated their review
    """

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    commentOne = models.CharField(max_length=350, default="")
    commentTwo = models.CharField(max_length=350, default="")
    commentThree = models.CharField(max_length=350, default="")
    commentFour = models.CharField(max_length=350, default="")
    time_updated = models.DateTimeField(auto_now_add=True)

    # def author(self):
    # anonymize
    #    return Student.objects.get(user=self.user).name

# class Comment(models.Model):
#     """
#     Represents all comments from a single associated review
#     Attributes:
#         comment (:obj:`ForeignKey`): all comments from single review
#     """
#     review = models.ForeignKey(Review, on_delete=models.deletion.CASCADE)