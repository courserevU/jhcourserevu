from django.test import TestCase
from course.models import Course
from course.models import Review

# Create your tests here.
class CourseModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
                name = "OOSE",
                description = "Object-Oriented Software Engineering",
                course_num = "EN.601.421",
                num_credits = "3",
                department = "Computer Science",
                level = "Upper level undergraduate",
                prerequisites = "Data Structures, UIMA or Full-Stack JS",
                corequisites = "None",
                school = "Whiting School of Engineering",
                campus = "Homewood",
                is_writing_intensive = "Yes",
                meeting_section = "2",
                size = 20,
                instructors = "Ali Madooei",
                semester = "FA2019"
        )

    def test_course_name(self):
        self.assertEqual(self.course.name, "OOSE")

    def test_course_des(self):
        self.assertEqual(self.course.description, "Object-Oriented Software Engineering")
    
    def test_course_num(self):
        self.assertEqual(self.course.course_num, "EN.601.421")
    
    def test_course_credits(self):
        self.assertEqual(self.course.num_credits, "3")
    
    def test_course_dept(self):
        self.assertEqual(self.course.department, "Computer Science")

    def test_course_level(self):
        self.assertEqual(self.course.level, "Upper level undergraduate")

    def test_course_prereq(self):
        self.assertEqual(self.course.prerequisites, "Data Structures, UIMA or Full-Stack JS")
    
    def test_course_coreq(self):
        self.assertEqual(self.course.corequisites, "None")

    def test_course_school(self):
        self.assertEqual(self.course.school, "Whiting School of Engineering")
    
    def test_course_campus(self):
        self.assertEqual(self.course.campus, "Homewood")

    def test_is_writing_intensive(self):
        self.assertEqual(self.course.is_writing_intensive, "Yes")

    def test_meeting_section(self):
        self.assertEqual(self.course.meeting_section, "2")

    def test_size(self):
        self.assertEqual(self.course.size, 20)
    
    def test_course_inst(self):
        self.assertEqual(self.course.instructors, "Ali Madooei")

    def test_semester(self):
        self.assertEqual(self.course.semester, "FA2019")

class ReviewModelTests(TestCase):

    def setup(self):
        self.review = Review.objects.create(
            course=Course.objects.create(name="OOSE",
                                         description="Object-Oriented Software Engineering",
                                         course_num="EN.601.421",
                                         num_credits="3",
                                         department="Computer Science",
                                         level="Upper level undergraduate",
                                         prerequisites="Data Structures, UIMA or Full-Stack JS",
                                         corequisites="None",
                                         school="Whiting School of Engineering",
                                         campus="Homewood",
                                         is_writing_intensive="Yes",
                                         meeting_section="2",
                                         size=20,
                                         instructors="Ali Madooei",
                                         semester="FA2019"),
            time_updated='Friday, March 18, 2022 4:24:50 PM'
        )

    def test_review_course(self):
        self.assertEqual(self.review.course, Course.objects.create(name="OOSE",
                                                                   description="Object-Oriented Software Engineering",
                                                                   course_num="EN.601.421",
                                                                   num_credits="3",
                                                                   department="Computer Science",
                                                                   level="Upper level undergraduate",
                                                                   prerequisites="Data Structures, UIMA or Full-Stack JS",
                                                                   corequisites="None",
                                                                   school="Whiting School of Engineering",
                                                                   campus="Homewood",
                                                                   is_writing_intensive="Yes",
                                                                   meeting_section="2",
                                                                   size=20,
                                                                   instructors="Ali Madooei",
                                                                   semester="FA2019")
                         )


    def test_review_time_updated(self):
        self.assertEqual(self.review.time_updated, 'Friday, March 18, 2022 4:24:50 PM')
