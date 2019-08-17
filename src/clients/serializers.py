from django.utils import timezone
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedModelSerializer,
    ValidationError,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField
)

from .models import Client, Contact


class ClientSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(
        read_only=True,
        view_name='accounts:user-detail',
    )

    class Meta:
        model = Client
        fields = [
            'user', 'name', 'surname', 'street',
            'city', 'country', 'phone', 'birthday',
        ]

    def validate_birthday(self, value):
        today = timezone.now().date()
        adult_date = today - timezone.timedelta(days=18 * 365)
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