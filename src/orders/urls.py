from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

router = DefaultRouter()
router.register('', OrderViewSet)

app_name = 'orders'

urlpatterns = router.urls
