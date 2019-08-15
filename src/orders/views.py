from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework import filters

from .models import Order
from .serializers import OrderSerializer, OrderRetrieveSerializer
from .paginations import StandardLimitPagination


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['product', 'amount']
    pagination_class = StandardLimitPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveSerializer
