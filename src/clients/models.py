from django.db import models


class Client(models.Model):
    name = models.CharField('Imię', max_length=250)
    surname = models.CharField('Nazwisko', max_length=250)
    street = models.CharField('Adres', max_length=1000, blank=True)
    city = models.CharField('Miasto', max_length=250, blank=True)
    country = models.CharField('Kraj', max_length=250, blank=True)
    phone = models.PositiveIntegerField('Numer tel.', null=True, blank=True)
