from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, F

from store.models import Collection, Order, OrderItem, Product


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
    query_set = Order.objects.select_related(
        'customer').order_by('-placed_at')[:5]

    return render(request, 'hello.html', {'name': 'Cyril', 'orders': list(query_set)})
