from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserRegisterAPIView, UserLoginAPIView, UserLogoutAPIView, DepartamentViewSet, UserViewSet)

app_name = 'accounts'

router = DefaultRouter()
router.register(r'departaments', DepartamentViewSet)
router.register(r'workers', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
]
