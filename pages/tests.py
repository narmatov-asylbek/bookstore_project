from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomepageTest(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_correct_template_usage(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_text_content(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)