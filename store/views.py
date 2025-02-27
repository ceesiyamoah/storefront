
from django.db.models.aggregates import Count
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import DefaultPagination
from .filters import ProductFilter
from .models import OrderItem, Product, Collection, Review
from .serializers import CollectionSerializer, ProductSerializer, ReviewSerializer
# Create your views here.


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    pagination_class = DefaultPagination

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count:
            return Response({'error': "Product can not be deleted because it is associated to a order"}, status=status.HTTP_405_METHOD_NOT_ALLOWED,)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    pagination_class = DefaultPagination
    search_fields = ['title']
    filter_backends = [SearchFilter]

    def destroy(self, request, *args, **kwargs):
        if Collection.objects.filter(products=kwargs['pk']).count:
            return Response({'error': "Collection can not be deleted because it is associated to a product"}, status=status.HTTP_405_METHOD_NOT_ALLOWED,)
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
