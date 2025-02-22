from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('collection/<int:pk>/', views.collection_detail, name='collection_detail'),
]
