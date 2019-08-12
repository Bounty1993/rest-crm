from django.urls import path, include

from .views import hello

app_name = 'clients'

urlpatterns = [
    path('', hello)
]