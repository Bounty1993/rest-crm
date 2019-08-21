import json
from django.test import TestCase
from django.urls import reverse

from src.accounts.models import Departament, User
from src.accounts.serializers import UserListSerializer


class AccountsViewsTest(TestCase):
    fixtures = ['src/accounts/tests/db.json']

    def setUp(self):
        self.test_user = User.objects.create_user(
            username='test_user', password='Tester123'
        )

    def test_register_correct(self):
        data = {
            'username': 'Bartosz2018', 'email': 'bartosz2018@onet.pl',
            'password': 'Tester123', 'password2': 'Tester123',
        }
        url = reverse('accounts:register')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        user = User.objects.filter(username='Bartosz2018')
        self.assertTrue(user.exists())
        password = data['password']
        self.assertTrue(user.first().check_password(password))

    def test_login_correct(self):
        data = {'username': 'test_user', 'password': 'Tester123'}
        url = reverse('accounts:login')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_login_incorrect(self):
        data = {'username': 'test_user', 'password': 'Wrong password'}
        url = reverse('accounts:login')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        actual_error = response.data['non_field_errors'][0]
        expected_error = 'Użytkownik lub hasło są nieprawidłowe'
        self.assertEqual(actual_error, expected_error)

    def test_logout(self):
        self.client.force_login(self.test_user)
        url = reverse('accounts:logout')
        self.client.get(url)
        with self.assertRaises(KeyError):
            auth_id = self.client.session['_auth_user_id']
    """
    def test_password_change(self):
        url = reverse('accounts:password_change')
        data = {
            'old_password': 'Wrong password', 'new_password': 'Tester321'
        }
        self.client.force_login(self.test_user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        data['old_password'] = 'Tester123'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        password = data['new_password']
        self.assertTrue(self.test_user.check_password(password))
    """

    def test_user_list(self):
        url = reverse('accounts:user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_detail_update_delete_correct(self):
        url = reverse('accounts:user-detail', kwargs={'pk': self.test_user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.force_login(self.test_user)
        data = {'email': 'nowyemail@gmail.com'}
        # response = self.client.put(url, data)
        # self.assertEqual(response.status_code, 200)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_user_update_delete_correct(self):
        url = reverse('accounts:user-detail', kwargs={'pk': self.test_user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 403)
