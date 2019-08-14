from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'name', 'surname', 'street',
            'city', 'country', 'phone',
        ]
