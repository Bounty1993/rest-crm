from django.db import models


class Order(models.Model):
    product = models.CharField('Produkt', max_length=50)
    amount = models.PositiveIntegerField('Ilość')
    price = models.DecimalField(
        decimal_places=2, max_digits=7
    )

    def __str__(self):
        return f'{self.product}'
