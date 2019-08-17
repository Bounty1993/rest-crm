from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    UserListSerializer, UserRegistrationSerializer,
    UserLoginSerializer, DepartamentSerializer)
from .permissions import IsServiceStaffOrReadOnly, IsOwnerOrReadOnly
from .models import Departament

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


class UserLogoutAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            logout(request)
            return redirect('/')
        return Response('Bad request')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    http_method_names = ['get', 'put', 'delete', 'head', 'options']
    permission_classes = [IsOwnerOrReadOnly]


class DepartamentViewSet(ModelViewSet):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    permission_classes = [IsAuthenticated, IsServiceStaffOrReadOnly]
