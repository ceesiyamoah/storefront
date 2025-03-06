from django.urls import path
from django.contrib import admin
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewset, basename='products')
router.register('collection', views.CollectionViewSet)
router.register('carts', views.CartViewSet, basename='carts')
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrdersViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product',)
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='carts-items')


urlpatterns = router.urls+products_router.urls+cart_router.urls
