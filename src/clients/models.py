from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Client(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Użytkownik',
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField('Imię', max_length=100)
    surname = models.CharField('Nazwisko', max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    street = models.CharField('Adres', max_length=1000, blank=True)
    city = models.CharField('Miasto', max_length=250, blank=True)
    country = models.CharField('Kraj', max_length=250, blank=True)
    phone = models.PositiveIntegerField(
        'Numer tel.', null=True, blank=True
    )
    email = models.EmailField(blank=True)
    birthday = models.DateField(blank=True, null=True)

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


class Contact(models.Model):
    KIND = (
        ('S', 'Sprzedaż'),
        ('M', 'Spotkanie'),
        ('B', 'Brak kontaktu'),
        ('I', 'Inne')
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
        verbose_name='użytkownik'
    )
    client = models.OneToOneField(
        Client, verbose_name='klient', on_delete=models.CASCADE
    )
    kind = models.CharField('Rodzaj', max_length=15, choices=KIND)
    subject = models.CharField('Tytuł', max_length=100)
    description = models.CharField('Opis', max_length=1000)
    creation_date = models.DateField('Data', auto_now_add=True)
    date = models.DateField('Zaplanowana data', blank=True, null=True)

    def __str__(self):
        return f'{self.creation_date - self.client}'
