from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import (
    UserListSerializer, UserRegistrationSerializer, UserLoginSerializer)

User = get_user_model()


class UserRegisterAPIView(CreateAPIView):
    queryser = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_obj = authenticate(request, username=data['username'], password=data['password'])
            login(request, user_obj)
            token = serializer.data
            return Response(token, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
