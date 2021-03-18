from django.test import TestCase
from django.urls.base import resolve
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your tests here.

class CustomUserTests(TestCase):
    
    def test_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='asyl',
            email = 'asyl@email.com',
            password = 'ilim0000'
        )
        self.assertEqual(user.username, 'asyl')
        self.assertEqual(user.email, 'asyl@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_superuser_creation(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='asylbek',
            email='asylbek@email.com',
            password='ilim0000'
        )

        self.assertEqual(admin_user.username, 'asylbek')
        self.assertEqual(admin_user.email, 'asylbek@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'
    
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Create an account')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
        self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)