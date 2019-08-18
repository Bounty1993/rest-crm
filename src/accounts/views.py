from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
)
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    UserListSerializer, UserRegistrationSerializer,
    UserLoginSerializer, DepartamentSerializer,
    ChangePasswordSerializer)
from .permissions import (
    IsServiceStaffOrReadOnly, IsOwnerOrReadOnly, HasDepartament
)
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


class PasswordChangeAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not user.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get("new_password"))
            user.save()
            update_session_auth_hash(request, user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    http_method_names = ['get', 'put', 'delete', 'head', 'options']
    permission_classes = [IsOwnerOrReadOnly]


class DepartamentViewSet(ModelViewSet):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    permission_classes = [IsAuthenticated, HasDepartament, IsServiceStaffOrReadOnly]
