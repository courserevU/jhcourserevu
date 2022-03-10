from django.test import TestCase

from user.models import User
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(jhed_id = 'jsmith0', jhed_email = 'jsmith0@jh.edu', class_year = 1990, perferred_name = 'j')

    def test_not_admin(self):
        """Default user is not admin"""
        default_user = User.objects.get(jhed_id="jsmith0")

        # self.assertEqual(default_user.speak(), 'The cat says "meow"')

    def test_admin(self):
        """User is admin"""

    def test_validate_email(self):
        """User does not exists without a valid email"""