import json
from django.test import TestCase

from src.accounts.models import Departament, User
from src.accounts.serializers import (
    UserRegistrationSerializer, UserLoginSerializer,
    UserListSerializer, ChangePasswordSerializer,
    DepartamentSerializer
)


class AccountsSerializersTest(TestCase):
    fixtures = ['src/accounts/tests/db.json']

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='bartosz99', password='Tester123'
        )

    def test_registration_correct(self):
        data = {
            'username': 'bartosz12',
            'email': 'bartosz@onet.pl',
            'password': 'Tester123',
            'password2': 'Tester123',
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        user = User.objects.filter(username='bartosz12')
        self.assertTrue(user.exists())
        user = user.first()
        self.assertEqual(user.username, 'bartosz12')
        self.assertTrue(user.check_password('Tester123'))

    def test_login_correct(self):
        data = {'username': 'bartosz99', 'password': 'Tester123'}
        serializer = UserLoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_login_incorrect(self):
        data = {'username': 'bartosz99', 'password': 'Tester100'}
        serializer = UserLoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        expected_error = 'Użytkownik lub hasło są nieprawidłowe'
        # self.assertEqual(serializer.errors['non_field_errors'], expected_error)

    def test_list_serializer(self):
        queryset = User.objects.all()
        serializer = UserListSerializer(data=queryset)
        user = serializer.initial_data[0]

    def test_change_password(self):
        data = {'old_password': 'Tester123', 'new_password': 'Tester321'}
        serializer = ChangePasswordSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        data['new_password'] = 'ABC'
        serializer = ChangePasswordSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_departament_serializer(self):
        data = {'name': 'IT'}
        serializer = DepartamentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        User.objects.all().delete()
        Departament.objects.all().delete()
        serializer = DepartamentSerializer(data=data)
        self.assertTrue(serializer.is_valid())
