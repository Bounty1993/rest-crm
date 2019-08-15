from django.db import models
from django.conf import settings

from src.clients.models import Client


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Użytkownik',
        on_delete=models.DO_NOTHING
    )
    client = models.ForeignKey(
        Client, verbose_name='Klient', on_delete=models.DO_NOTHING
    )
    product = models.CharField('Produkt', max_length=50)
    amount = models.PositiveIntegerField('Ilość')
    price = models.DecimalField(
        decimal_places=2, max_digits=7
    )
    date = models.DateField(auto_now_add=True)
    delivery = models.DateField()

    def __str__(self):
        return f'{self.product}'
