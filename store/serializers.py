from decimal import Decimal
from rest_framework import serializers


from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_tax', 'collection']
        # fields="__all__"
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        return product.unit_price*Decimal(1.1)

    # used to override validation
    def validate(self, attrs):
        return super().validate(attrs)
