# pages/tests.py
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from market import views


class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('market:homepage'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('market:homepage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/home.html','market/base.html')

    # def test_home_page_contains_correct_html(self):
    #     response = self.client.get('/')
    #     self.assertContains(response, '<h1>Homepage</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')









