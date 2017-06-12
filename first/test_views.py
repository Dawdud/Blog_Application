from django.test import TestCase
from django.urls import reverse
class AboutTest(TestCase):
    def test_about(self):
        resp= self.client.get('/first/about/')
        self.assertEqual(resp.status_code,200)

class LogoutTest(TestCase):
    def test_logout(self):
        resp= self.client.get('/first/logout/')
        self.assertEqual(resp.status_code, 200)

class indexTest(TestCase):
     def test_index(self):
         resp= self.client.get('/first/')
         self.assertEqual(resp.status_code, 200)
