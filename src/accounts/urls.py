from django.urls import path

from .views import (
    UserListAPIView, UserRegisterAPIView, UserLoginAPIView)

app_name = 'accounts'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
]