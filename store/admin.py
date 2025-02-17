from django.contrib import admin

from store.models import Address, Cart, CartItem, Collection, Customer, Order, OrderItem, Product
from tags.models import Tag, TaggedItem
from django.db.models import Count
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 20
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']

    @admin.display(ordering='orders_count')
    def orders_count(self, customer):
        url = f'{reverse('admin:store_order_changelist')}?{urlencode({'customer__id': str(customer.id)})}'
        return format_html("<a href={}>{}</a>", url, customer.orders_count)
        return customer.orders_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'payment_status', 'customer_name']
    list_select_related = ['customer']

    @admin.display(ordering='customer__first_name')
    def customer_name(self, product):
        return f'{product.customer.first_name} {product.customer.last_name}'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = f'{reverse('admin:store_product_changelist')}?{urlencode({'collection__id': str(collection.id)})}'
        return format_html("<a href={}>{}</a>", url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


admin.site.register(OrderItem)
admin.site.register(Tag)
admin.site.register(TaggedItem)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
