from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(soeid='TEST', password='testpass', email='test@citi.com'):
    """Create a sample user"""
    return get_user_model().objects.create_user(soeid, password, email)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        soeid = 'TEST'
        password = 'Testpass123'
        email = 'test@citi.com'
        user = get_user_model().objects.create_user(
            soeid=soeid,
            password=password,
            email=email
        )

        self.assertEqual(user.soeid, soeid)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        soeid = 'TEST'
        email = 'test@citi.com'
        user = get_user_model().objects.create_user(soeid, 'test123', email)

        self.assertEqual(user.soeid, soeid.upper())
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123', None)

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'TEST',
            'test123',
            'test@citi.com'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    # def test_tag_str(self):
    #     """Test the tag string representation"""
    #     tag = models.Tag.objects.create(
    #         user=sample_user(),
    #         name='Vegan'
    #     )

    #     self.assertEqual(str(tag), tag.name)

    # def test_ingredient_str(self):
    #     """Test the ingredient string representation"""
    #     ingredient = models.Ingredient.objects.create(
    #         user=sample_user(),
    #         name='Cucumber'
    #     )

    #     self.assertEqual(str(ingredient), ingredient.name)

    # def test_recipe_Str(self):
    #     """Test the recipe string representation"""
    #     recipe = models.Recipe.objects.create(
    #         user=sample_user(),
    #         title='Steak and mushroom sauce',
    #         time_minutes=5,
    #         price=5.00
    #     )

    #     self.assertEqual(str(recipe), recipe.title)

    # @patch('uuid.uuid4')
    # def test_recipe_file_name_uuid(self, mock_uuid):
    #     """Test that image is saved in the correct location"""
    #     uuid = 'test-uuid'
    #     mock_uuid.return_value = uuid
    #     file_path = models.resource_file_path(None, 'myimage.jpg')

    #     exp_path = f'uploads/recipe/{uuid}.jpg'
    #     self.assertEqual(file_path, exp_path)
