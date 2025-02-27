from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models.aggregates import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from store import serializers
from store.filters import ProductFilter
from store.models import OrderItem, Product, Collection, Review
from store.serializers import CollectionSerializer, ProductSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    queryset = Product.objects.all()

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
