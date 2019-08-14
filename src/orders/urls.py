from django.urls import path, include

from .views import OrderListAPIView, OrderCreateAPIView, OrderRetrieveAPIView

app_name = 'orders'
urlpatterns = [
    path('', OrderListAPIView.as_view(), name='list'),
    path('create/', OrderCreateAPIView.as_view(), name='create'),
    path('<pk>/', OrderRetrieveAPIView.as_view(), name='retrive'),
]
