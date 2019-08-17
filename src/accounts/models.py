from django.db import models
from django.contrib.auth.models import AbstractUser


class Departament(models.Model):
    DEPARTAMENTS = (
        ('S', 'Sprzedaż'),
        ('IT', 'Wsparcie techniczne'),
    )

    name = models.CharField(max_length=30, choices=DEPARTAMENTS)

    def __str__(self):
        return self.name


class User(AbstractUser):
    departament = models.ForeignKey(
        Departament, related_name='workers',
        on_delete=models.DO_NOTHING, blank=True, null=True
    )
    chef = models.ForeignKey(
        'self', on_delete=models.DO_NOTHING,
        related_name='workers', blank=True, null=True
    )
