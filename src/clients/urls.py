from django.urls import path, include

from rest_framework import routers

from .views import ClientViewSet, ContactViewSet

app_name = 'clients'

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = router.urls