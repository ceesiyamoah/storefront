from django.urls import path
from django.contrib import admin
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewset, basename='products')
router.register('collection', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product',)
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')


urlpatterns = router.urls+products_router.urls
