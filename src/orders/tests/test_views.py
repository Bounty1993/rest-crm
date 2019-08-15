from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..serializers import OrderSerializer, OrderCreateSerializer
from ..models import Order
from src.clients.models import Client

User = get_user_model()


class OrderViewTest(TestCase):
    fixtures = ['db.json']

    def setUp(self):
        self.user = User.objects.first()
        self.client_ = Client.objects.first()
        self.create_data = {
            'user': self.user.id,
            'client': self.client_.id,
            'product': 'Batonik',
            'amount': 100,
            'price': 150.05,
            'delivery': '2019-09-10'
        }

    def test_list_status_code(self):
        url = reverse('orders:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_no_auth(self):
        url = reverse('orders:list')
        response = self.client.post(url, self.create_data)
        self.assertEqual(response.status_code, 403)

    def test_create_view_correct(self):
        self.client.force_login(self.user)
        url = reverse('orders:list')
        response = self.client.post(url, self.create_data)
        self.assertEqual(response.status_code, 201)