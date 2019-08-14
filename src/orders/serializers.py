from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'product',
            'amount',
            'price',
        ]


class OrderRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'product',
            'amount',
            'price',
        ]