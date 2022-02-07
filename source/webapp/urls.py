from django.urls import path


from webapp.views import ProductList, ProductView, ProductCreate, ProductUpdate, ProductDelete, CartCreate

urlpatterns = [
     path('', ProductList.as_view(), name="index"),
     path('product/<int:pk>/', ProductView.as_view(), name="product_view"),
     path('product/add/', ProductCreate.as_view(), name='product_add'),
     path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
     path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
     path('cart/', CartCreate.as_view(), name='cart')
]