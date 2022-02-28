from django.urls import path


from webapp.views import ProductList, ProductView, ProductCreate, ProductUpdate, ProductDelete, CartCreate, CartView, \
     CartDeleteView, CartDeleteOneView, OrderCreateView, OrdersView

app_name = "webapp"

urlpatterns = [
     path('', ProductList.as_view(), name="index"),
     path('product/<int:pk>/', ProductView.as_view(), name="product_view"),
     path('product/add/', ProductCreate.as_view(), name='product_add'),
     path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
     path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
     path('product/<int:pk>/add-to-cart/', CartCreate.as_view(), name='product_add_to_cart'),
     path('cart', CartView.as_view(), name='cart_view'),
     path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete_view'),
     path('cart/<int:pk>/delete-one/', CartDeleteOneView.as_view(), name='cart_delete_one_view'),
     path('order/create/', OrderCreateView.as_view(), name='order_create_view'),
     path('orders/', OrdersView.as_view(), name='orders_view')
]