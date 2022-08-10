# from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# all functions must start with test_
# the name, even if long, should be as descriptive as possible.

class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_templates(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "index.html")
# Create your tests here.
    def test_about_page_uses_correct_templates(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "about.html")


    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"index.html")

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"about.html")

    def test_home_page_contains_text(self):
        response = self.client.get("/")
        self.assertContains(response,"Success!")

    def test_about_page_contains_text(self):
        response = self.client.get("/about/")
        self.assertContains(response,"learning django")