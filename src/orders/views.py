from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from .models import Order
from .serializers import OrderSerializer, OrderRetrieveSerializer


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveSerializer



