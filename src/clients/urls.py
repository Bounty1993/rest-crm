from django.urls import path, include

from .views import Hello

app_name = 'clients'

urlpatterns = [
    path('', Hello.as_view())
]