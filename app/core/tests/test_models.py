from django.contrib.auth import get_user_model
from django.test import TestCase

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email ='test@gmail.com'
        password= 'Testpass123'
        user= get_user_model().objects.create_user(
            email=email,
            password= password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email= 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email,"Test1234")
        self.assertEqual(user.email, email.lower())
    
    def test_new_invalid_email(self):
        """Testing creating user without email errors"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "234h9okhh")
    
    def test_creating_super_user(self):
        """Testing creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "abcd1234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)