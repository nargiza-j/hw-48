from django.urls import path

from webapp.views.product_views import product_delete_view, \
     product_update_view, ProductList, ProductView, ProductCreate

urlpatterns = [
     path('', ProductList.as_view(), name="index"),
     path('product/<int:pk>/', ProductView.as_view(), name="product_view"),
     path('product/add/', ProductCreate.as_view(), name='product_add'),
     path('product/<int:pk>/delete/', product_delete_view, name='product_delete'),
     path('product/<int:pk>/update/', product_update_view, name='product_update')
]