from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

class TestCustomUser(TestCase):
    
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
