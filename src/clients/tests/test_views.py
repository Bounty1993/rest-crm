from django.test import TestCase
from django.urls import reverse


class ViewsTests(TestCase):
    def test_get(self):
        url = reverse('clients:client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_no_client(self):
        url = reverse('clients:client-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
