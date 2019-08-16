from django.utils import timezone
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    HyperlinkedIdentityField
)

from .models import Client


class ClientSerializer(ModelSerializer):
    user = HyperlinkedIdentityField(
        view_name='accounts:detail',
        lookup_field='pk'
    )

    class Meta:
        model = Client
        fields = [
            'user', 'name', 'surname', 'street',
            'city', 'country', 'phone', 'birthday',
        ]

    def validate_birthday(self, value):
        today = timezone.now().date()
        adult_date = today - timezone.timedelta(years=18)
        if adult_date < value:
            msg = 'Klient nie jest pełnoletni'
            raise ValidationError(msg)
        return value