from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import (
    ValidationError,
    HyperlinkedIdentityField,
    SlugRelatedField,
    SerializerMethodField
)
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='orders:detail',
    )
    user = SerializerMethodField()
    client = SerializerMethodField()
    total_value = SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'url',
            'id',
            'user',
            'client',
            'product',
            'amount',
            'price',
            'delivery',
            'total_value',
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_client(self, obj):
        name = obj.client.name
        surname = obj.client.surname
        full_name = f'{name} {surname}'
        return full_name

    def get_total_value(self, obj):
        return obj.total_value

    def validate_delivery(self, value):
        today = timezone.now().date()
        if value < today:
            msg = 'Data dostawy nie może być w przeszłości'
            raise ValidationError(msg)
        return value


class OrderRetrieveSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'user',
            'client',
            'product',
            'amount',
            'price',
        ]

    def get_user(self, obj):
        return str(obj.user.username)
