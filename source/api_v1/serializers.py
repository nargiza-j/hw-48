from rest_framework import serializers

from webapp.models import Product, OrderProduct, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "category", "remainder", "price")


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product', 'qty')


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('user', 'name', 'phone', 'address', 'created_at', 'order_products')