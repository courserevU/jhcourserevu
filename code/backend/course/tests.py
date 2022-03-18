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
    """course = models.ForeignKey(Course, on_delete=models.CASCADE)
    comments = models.CharField(max_length=350, default="")
    work = models.CharField(max_length=350, default="")
    workload = models.CharField(max_length=350, default="")
    assignment_style = models.CharField(max_length=350, default="")
    exam_style = models.CharField(max_length=350, default="")
    outside_time = models.CharField(max_length=350, default="")
    teaching_style = models.CharField(max_length=350, default="")
    teaching_effectiveness = models.CharField(max_length=350, default="")
    prof_availability = models.CharField(max_length=350, default="")
    grading_style = models.CharField(max_length=350, default="")
    time_updated = models.DateTimeField(auto_now_add=True)"""
    def setup(self):
        Review.objects.create(
            course='OOSE',
            comments='This class is great.',
            time_updated='Friday, March 18, 2022 4:24:50 PM'
        )
    def test_review_course(self):
        pass
    def test_review_comments(self):
        pass
    def test_review_time_updated(self):
        pass

