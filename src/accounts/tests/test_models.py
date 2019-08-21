from django.test import TestCase

from src.accounts.models import Departament, User


class ModelsTest(TestCase):
    fixtures = ['src/accounts/tests/db.json']

    def test_departament_str(self):
        it_departament = Departament.objects.get(name='IT')
        self.assertEqual(str(it_departament), 'IT')

    def test_user_str(self):
        user = User.objects.get(username='bartosz')
        self.assertEqual(str(user), 'bartosz')
