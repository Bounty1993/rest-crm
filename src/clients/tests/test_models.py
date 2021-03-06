from django.test import TestCase

from ..models import Client
from src.accounts.models import User


class ClientTest(TestCase):
    fixtures = ['src/clients/tests/db.json']

    def setUp(self):
        self.test_user = User.objects.first()
        self.obj = Client.objects.create(
            user = self.test_user,
            name='Bartek', surname='Tester', street='Test Ulica',
            city='Waw', country='Polska', phone=48226974040,
            birthday='1993-05-05'
        )

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

    def test_save(self):
        slug = self.obj.slug
        self.assertEqual(slug, self.obj.slug)
        self.new_obj = Client.objects.create(
            name='Bartek', surname='Tester', user=self.test_user
        )
        self.assertEqual(self.new_obj.slug, 'bartek-tester-1')
        self.obj.name = 'Tomek'
        self.obj.save()
        self.assertEqual(self.obj.slug, 'tomek-tester')
