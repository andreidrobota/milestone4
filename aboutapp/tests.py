from django.test import TestCase
from django.urls import reverse
from .models import AboutApp

# Create your tests here.

class TestAboutUsView(TestCase):

    def setUp(self):
        self.about_content = AboutApp(
            title="About Us", content="This is about us section.")
        self.about_content.save()