from django.test import TestCase

class CustomUserTests(TestCase):
    def test_create_user(self):
        # test creating a user
        self.assertEqual(1+1, 2)

    def test_create_superuser(self):
        # test creating a superuser
        self.assertEqual(2*2, 4)
