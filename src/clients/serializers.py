from django.utils import timezone
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    HyperlinkedIdentityField
)

from .models import Client, Contact


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
            'slug',
        ]

    def validate_birthday(self, value):
        today = timezone.now().date()
        adult_date = today - timezone.timedelta(years=18)
        if adult_date < value:
            msg = 'Klient nie jest pełnoletni'
            raise ValidationError(msg)
        return value


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'client', 'user', 'kind',
            'subject', 'description',
            'creation_date', 'date',
        ]
        extra_kwargs = {
            'client': {'read_only': True},
            'user': {'read_only': True},
        }

    def validate_date(self, value):
        today = timezone.now().date()
        if value < today:
            msg = 'Date nie może być w przeszłości'
            raise ValidationError(msg)
        return value