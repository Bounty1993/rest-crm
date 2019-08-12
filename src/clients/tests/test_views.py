from django.test import TestCase


class ViewsTests(TestCase):
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)