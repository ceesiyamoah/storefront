from decimal import Decimal
from rest_framework import serializers


from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory',
                  'description', 'unit_price', 'price_with_tax', 'collection']
        # fields="__all__"
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    # collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        return product.unit_price*Decimal(1.1)

    # used to override validation
    def validate(self, attrs):
        return super().validate(attrs)

    # override creation
    # def create(self, validated_data):
    #     product=Product(**validated_data)
    #     product.other=1
    #     product.save()
    #     return product

    # override update
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
