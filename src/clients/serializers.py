from django.utils import timezone
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    ValidationError,
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField
)

from .models import Client, Contact


class ContactSerializer(ModelSerializer):
    client = HyperlinkedRelatedField(
        view_name='clients:client-detail',
        lookup_field='slug',
        queryset=Client.objects.all()
    )

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


class ClientSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='clients:client-detail',
        lookup_field='slug',
    )
    user = HyperlinkedRelatedField(
        read_only=True,
        view_name='accounts:user-detail',
    )
    profits = SerializerMethodField()

    class Meta:
        model = Client
        fields = [
            'url', 'user', 'name',
            'surname', 'street', 'city',
            'country', 'phone', 'birthday',
            'email', 'profits',
        ]

    def get_profits(self, obj):
        profits = 0
        for order in obj.orders.all():
            profits += order.total_value
        return profits

    def validate_birthday(self, value):
        today = timezone.now().date()
        adult_date = today - timezone.timedelta(days=18 * 365)
        if adult_date < value:
            msg = 'Klient nie jest pełnoletni'
            raise ValidationError(msg)
        return value