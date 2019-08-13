from django.test import TestCase

from ..models import Client


class ClientTest(TestCase):
    def setUp(self):
        self.obj = Client.objects.create(
            name='Bartek', surname='Tester', street='Test Ulica',
            city='Waw', country='Polska', phone=48226974040)

    def test_creation(self):
        self.assertEqual(Client.objects.count(), 1)

    def test_data_correct(self):
        obj = self.obj
        self.assertEqual(obj.name, 'Bartek')
        self.assertEqual(obj.surname, 'Tester')
        self.assertEqual(obj.street, 'Test Ulica')
        self.assertEqual(obj.city, 'Waw')
        self.assertEqual(obj.country, 'Polska')
        self.assertEqual(obj.phone, 48226974040)
