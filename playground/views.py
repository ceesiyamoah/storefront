from django.forms import DecimalField, model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F, Value, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat

from store.models import Collection, Customer, Order, OrderItem, Product

from django.contrib.contenttypes.models import ContentType

from tags.models import TaggedItem
from django.db import transaction


def say_hello(request):
    # query_set = Product.objects.filter(
    # unit_price__range=(20, 25)
    # description__icontains='MA'
    # collection__id=3
    # last_update__year=2021
    # slug__isnull=True
    # )

    # query_set = Product.objects.filter(
    #     Q(description__icontains='MA') | Q(unit_price__range=(20, 25)))
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    # query_set = Product.objects.earliest('unit_price')

    # query_set = Product.objects.values('id')
    # query_set_orderItem = OrderItem.objects.values('product_id').distinct(
    # )
    # query_set = Product.objects.filter(
    #     id__in=query_set_orderItem).order_by('title')

    # query_set = Product.objects.select_related('collection').all() for 1 instance
    #  query_set = Product.objects.prefetch_related('promotions').all() for many to many objects
    # you can chain select_related and prefetch_related

    # query_set = Product.objects.select_related('collection').all()
    # query_set = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min(
    #     'unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))

    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(
    #         ' '), F('last_name'), function='CONCAT')
    # )
    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    # queryset = Customer.objects.annotate(
    #     orders_count=Count('order')
    # )
    # discounted_price = ExpressionWrapper(
    #     F('unit_price')*0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(
    #     discounted_price=discounted_price
    # )

    # queryset = TaggedItem.objects.get_tags_for(Product, 1)
    # collection = Collection()
    # collection.title = 'Video Games'
    # collection.featured_products = Product(id=1)
    # collection.save()
    # Collection.objects.create()

    # updating
    # collection = Collection.objects.get(pk=11)
    # collection.title = 'Big Bangers'
    # collection.featured_products = None
    # collection.save()
    # Collection.objects.filter(pk=11).update(title='Winner')

    # deleting objects
    # collection = Collection(pk=12)
    # collection.delete()
    # multiple
    # Collection.objects.filter()

    # transactions
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 4
    #     item.save()

    # raw sql
    # queryset = Product.objects.raw('SELECT * FROM store_product')

    return render(request, 'hello.html', {'name': 'Cyril', 'result': []})
