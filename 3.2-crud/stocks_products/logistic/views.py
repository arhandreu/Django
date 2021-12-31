import django_filters
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class StockFilter(django_filters.rest_framework.FilterSet):
    product = django_filters.CharFilter(field_name='products__title', lookup_expr='contains')
    description = django_filters.CharFilter(field_name='products__description', lookup_expr='contains')

    class Meta:
        model = Stock
        fields = ['product', 'description']




class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', ]
    search_fields = ['title', 'description', ]
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['products', ]
    # search_fields = ['product', ]
    filter_class = StockFilter
    # при необходимости добавьте параметры фильтрации
