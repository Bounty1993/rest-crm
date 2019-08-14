from django.db import models
from django.utils.text import slugify


class Client(models.Model):
    name = models.CharField('Imię', max_length=100)
    surname = models.CharField('Nazwisko', max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    street = models.CharField('Adres', max_length=1000, blank=True)
    city = models.CharField('Miasto', max_length=250, blank=True)
    country = models.CharField('Kraj', max_length=250, blank=True)
    phone = models.PositiveIntegerField('Numer tel.', null=True, blank=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        slug = slugify(f'{self.name} {self.surname}')
        num = 1
        while True:
            obj = Client.objects.filter(slug=slug)
            if not obj.exists():
                break
            elif obj.first().id == self.id:
                break
            else:
                slug += f'-{num}'
                num += 1
        self.slug = slug
        super().save(*args, **kwargs)
