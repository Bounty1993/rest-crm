from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework import filters
from .models import Order
from .serializers import OrderSerializer
from .paginations import StandardLimitPagination


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['product', 'amount']
    pagination_class = StandardLimitPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
