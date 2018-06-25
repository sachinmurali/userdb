from django.test import TestCase
from .models import User
# Create your tests here.


class ModelTestCase(TestCase):
    def setUp(self):
        """Summary
        """
        self.email = 'sachinmurali92@gmail.com'
        self.name = 'An app to create a user database'
        self.userdb = User(email=self.email, name=self.name)

    def test_model_can_create_a_user(self):
        """Summary
        """
        initial_count = User.objects.count()
        self.userdb.save()
        current_count = User.objects.count()
        self.assertNotEqual(initial_count, current_count)
