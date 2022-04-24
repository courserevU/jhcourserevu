from django.test import TestCase

from django.contrib.auth.models import User as django_user
from user.models import User
from course.models import Course
import re
# Create your tests here.

class UserTestCase(TestCase):
    
    def setUp(self):
        self.user = django_user.objects.create_user(username="john", password="pass")
        self.courses = Course.objects.create(name="OOSE",
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
        self.jhed_id = 'jsmith0'
        self.jhed_email = 'jsmith0@jhu.edu'
        self.class_year = 1990
        self.preferred_name = 'j'
        self.is_admin = False
        # User.objects.create(user = null,
        #                     courses = null,
        #                     jhed_id = 'jsmith0',
        #                     jhed_email = 'jsmith0@jh.edu',
        #                     class_year = 1990,
        #                     preferred_name = 'j',
        #                     is_admin = False)
    def test_user_jhed_id(self):
        self.assertEqual(self.jhed_id, 'jsmith0')

    def test_user_jhed_email(self):
        self.assertEqual(self.jhed_email, 'jsmith0@jhu.edu')

    def test_user_class_year(self):
        self.assertEqual(self.class_year, 1990)

    def test_user_preferred_name(self):
        self.assertEqual(self.preferred_name, 'j')

    def test_not_admin(self):
        """Default user is not admin"""
        default_user = User.objects.get(jhed_id="jsmith0")
        # update this later as necessary based on flag
        self.assertEqual(self.is_admin, False)

    def test_admin(self):
        """User is admin"""
        self.assertEqual(self.is_admin, False)

    # def test_validate_email(self):
    #     """User does not exists without a valid email"""
    #     email = self.jhed_email
    #     regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@jhu.edu')
    #     if re.fullmatch(regex, email):
    #         pass
    #     else:
    #         # Error message for invalid email - update later
    #         print('Invalid email')
