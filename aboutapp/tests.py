from django.test import TestCase
from django.urls import reverse
from .models import AboutApp
from .forms import WorkRequestForm

# Create your tests here.

class TestAboutUsView(TestCase):

    def setUp(self):
        self.about_content = AboutApp(
            title="About Us", content="This is about us section.")
        self.about_content.save()


class WorkRequestFormTests(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Tester Test',
            'email': 'testertest@example.com',
            'about_me': 'I am a software developer.',
            'why_us': 'I want to work with your team because...',
        }
        form = WorkRequestForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_data(self):
        form_data = {}
        form = WorkRequestForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_invalid_email(self):
        form_data = {
            'name': 'Tester Test',
            'email': 'invalid_email',
            'about_me': 'I am a software developer.',
            'why_us': 'I want to work with your team because...',
        }
        form = WorkRequestForm(data=form_data)
        self.assertFalse(form.is_valid())