from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
