from django.urls import path, include

from .views import OrderListCreateAPIView, OrderRetrieveAPIView

app_name = 'orders'
urlpatterns = [
    path('', OrderListCreateAPIView.as_view(), name='list'),
    path('<pk>/', OrderRetrieveAPIView.as_view(), name='detail'),
]
