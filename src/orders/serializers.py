from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import (
    ValidationError,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    SlugRelatedField,
    SerializerMethodField
)
from .models import Order
from src.clients.models import Client


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='orders:order-detail',
    )
    user = HyperlinkedRelatedField(
        view_name='accounts:user-detail',
        read_only=True
    )
    client = HyperlinkedRelatedField(
        view_name='clients:client-detail',
        queryset=Client.objects.all(),
        lookup_field='slug'
    )
    client_name = SerializerMethodField()
    total_value = SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'url', 'user', 'client',
            'client_name', 'product', 'amount',
            'price', 'delivery', 'total_value',
        ]
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def get_client_name(self, obj):
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
