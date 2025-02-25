from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('collection/', views.CollectionList.as_view()),
    path('collection/<int:pk>/', views.CollectionDetail.as_view(),
         name='collection_detail'),
]
