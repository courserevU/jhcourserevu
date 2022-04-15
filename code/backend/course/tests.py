from django.test import TestCase
from course.models import Course
from course.models import Review

# Create your tests here.
class CourseModelTests(TestCase):
    def setUp(self):
        self.name = "OOSE"
        self.description = "Object-Oriented Software Engineering"
        self.course_num = "EN.601.421"
        self.num_credits = "3"
        self.department = "Computer Science"
        self.level = "Upper level undergraduate"
        self.prerequisites = "Data Structures, UIMA or Full-Stack JS"
        self.corequisites = "None"
        self.school = "Whiting School of Engineering"
        self.campus = "Homewood"
        self.is_writing_intensive = "Yes"
        self.meeting_section = "2"
        self.size = 20
        self.instructors = "Ali Madooei"
        self.semester = "FA2019"

    def test_course_name(self):
        self.assertEqual(self.name, "OOSE")

    def test_course_des(self):
        self.assertEqual(self.description, "Object-Oriented Software Engineering")
    
    def test_course_num(self):
        self.assertEqual(self.course_num, "EN.601.421")
    
    def test_course_credits(self):
        self.assertEqual(self.num_credits, "3")
    
    def test_course_dept(self):
        self.assertEqual(self.department, "Computer Science")

    def test_course_level(self):
        self.assertEqual(self.level, "Upper level undergraduate")

    def test_course_prereq(self):
        self.assertEqual(self.prerequisites, "Data Structures, UIMA or Full-Stack JS")
    
    def test_course_coreq(self):
        self.assertEqual(self.corequisites, "None")

    def test_course_school(self):
        self.assertEqual(self.school, "Whiting School of Engineering")
    
    def test_course_campus(self):
        self.assertEqual(self.campus, "Homewood")

    def test_is_writing_intensive(self):
        self.assertEqual(self.is_writing_intensive, "Yes")

    def test_meeting_section(self):
        self.assertEqual(self.meeting_section, "2")

    def test_size(self):
        self.assertEqual(self.size, 20)
    
    def test_course_inst(self):
        self.assertEqual(self.instructors, "Ali Madooei")

    def test_semester(self):
        self.assertEqual(self.semester, "FA2019")

class ReviewModelTests(TestCase):

    def setup(self):
        Review.objects.create(
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
        # Review.objects.create(
        #     course='OOSE',
        #     comments='This class is great.',
        #     work='one group project',
        #     workload='8 hrs/week',
        #     assignment_style='coding, documentation',
        #     exam_style='only one quiz',
        #     outside_time='couple hours a week',
        #     teaching_style='learn through project',
        #     teaching_effectiveness='very effective',
        #     prof_availability='accessible via slack/class',
        #     grading_style='group grade',
        #     time_updated='Friday, March 18, 2022 4:24:50 PM'
        # )

    def test_review_course(self):
        self.assertEqual(self.course, 'OOSE')

    # def test_review_comments(self):
    #     self.assertEqual(self.comments, 'This class is great.')
    #
    # def test_review_work(self):
    #     self.assertEqual(self.work, 'one group project')
    #
    # def test_review_workload(self):
    #     self.assertEqual(self.workload, '8 hrs/week')
    #
    # def test_review_assignment_style(self):
    #     self.assertEqual(self.assignment_style, 'coding, documentation')
    #
    # def test_review_exam_style(self):
    #     self.assertEqual(self.exam_style, 'only one quiz')
    #
    # def test_review_outside_time(self):
    #     self.assertEqual(self.outside_time, 'couple hours a week')
    #
    # def test_review_teaching_style(self):
    #     self.assertEqual(self.teaching_style, 'learn through project')
    #
    # def test_review_teaching_effectiveness(self):
    #     self.assertEqual(self.teaching_effectiveness, 'very effective')
    #
    # def test_review_prof_availability(self):
    #     self.assertEqual(self.prof_availability, 'accessible via slack/class')
    #
    # def test_review_grading_style(self):
    #     self.assertEqual(self.grading_style, 'group grade')

    def test_review_time_updated(self):
        self.assertEqual(self.time_updated, 'Friday, March 18, 2022 4:24:50 PM')
