from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import (
    ValidationError,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='orders:detail',
    )
    user = SerializerMethodField()

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
        ]

    def get_user(self, obj):
        return str(obj.user.username)

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
