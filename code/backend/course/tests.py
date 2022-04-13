from django.test import TestCase
from course.models import Course
from course.models import Review

# Create your tests here.
class CourseModelTests(TestCase):
    def setUp(self):
        Course.objects.create(name = "OOSE", 
                              description = "Object-Oriented Software Engineering",
                              course_num = "EN.601.421",
                              num_credits = 3,
                              department = "Computer Science",
                              level = "Upper level undergraduate",
                              prerequisites = "Data Structures, UIMA or Full-Stack JS",
                              corequisites = "None",
                              school = "Whiting School of Engineering",
                              campus = "Homewood", 
                              notes = "Project-based",
                              info = "A course for OOSE",
                              exclusions = "No exclusions",
                              instructors = "Ali Madooei") 

    def test_course_name(self):
        self.assertEqual(self.name, "OOSE")

    def test_course_des(self):
        self.assertEqual(self.description, "Object-Oriented Software Engineering")
    
    def test_course_num(self):
        self.assertEqual(self.course_num, "EN.601.421")
    
    def test_course_credits(self):
        self.assertEqual(self.num_credits, 3)
    
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
    
    def test_course_notes(self):
        self.assertEqual(self.notes, "Project-based")
    
    def test_course_info(self):
        self.assertEqual(self.info, "A course for OOSE")
    
    def test_course_excl(self):
        self.assertEqual(self.exclusions, "No exclusions")
    
    def test_course_inst(self):
        self.assertEqual(self.instructors, "Ali Madooei")

class ReviewModelTests(TestCase):

    def setup(self):
        Review.objects.create(
            course='OOSE',
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
