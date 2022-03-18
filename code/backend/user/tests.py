from django.test import TestCase

from user.models import User
import re
# Create your tests here.

class UserTestCase(TestCase):
    
    def setUp(self):
        User.objects.create(jhed_id = 'jsmith0',
                            jhed_email = 'jsmith0@jh.edu',
                            class_year = 1990,
                            preferred_name = 'j',
                            is_admin = False)
    def test_user_jhed_id(self):
        self.assertEqual(self.jhed_id, 'jsmith0')

    def test_user_jhed_email(self):
        self.assertEqual(self.jhed_email, 'jsmith0@jh.edu')

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

    def test_validate_email(self):
        """User does not exists without a valid email"""
        email = self.jhed_email
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@jhu.edu')
        if re.fullmatch(regex, email):
            pass
        else:
            # Error message for invalid email - update later
            print('Invalid email')
