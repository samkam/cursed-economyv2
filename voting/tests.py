from django.test import TestCase
from django.urls import resolve
from voting.views import home_page
class ViewTest(TestCase):
	def test_renders_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

class ModelTest(TestCase):
	pass