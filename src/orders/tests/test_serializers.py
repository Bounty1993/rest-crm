from django.test import TestCase
from django.contrib.auth import get_user_model

from ..serializers import OrderSerializer
from ..models import Order
from src.clients.models import Client

User = get_user_model()


class OrderSerializerTest(TestCase):
    fixtures = ['db.json']

    def setUp(self):
        self.user = User.objects.first()
        self.client_ = Client.objects.first()

    def test_correct(self):
        data = {
            'user': self.user.id,
            'client': self.client_.id,
            'product': 'Batonik',
            'amount': 100,
            'price': 150.05,
            'delivery': '2019-09-10'
        }
        s = OrderSerializer(data=data)
        self.assertTrue(s.is_valid())
