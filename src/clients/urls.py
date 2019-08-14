from django.urls import path, include

from rest_framework import routers

from .views import ClientViewSet

app_name = 'clients'

router = routers.DefaultRouter()
router.register(r'', ClientViewSet)

urlpatterns = router.urls