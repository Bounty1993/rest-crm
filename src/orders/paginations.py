from rest_framework.pagination import LimitOffsetPagination


class StandardLimitPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100
