from django.test import TestCase
from django.urls.base import resolve
from django.urls import reverse
from django.contrib.auth import get_user_model


from users.forms import CustomUserCreationForm
from users.views import SignupPageView
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
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Create an account')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)