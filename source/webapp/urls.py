from django.urls import path

from webapp.views import index_view, product_view, create_product_view

urlpatterns = [
     path('', index_view, name="index"),
     path('product/<int:pk>/', product_view, name="product_view"),
     path('product/add/', create_product_view, name='product_add')
]