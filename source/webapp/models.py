from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import F, ExpressionWrapper as E, Sum
from django.urls import reverse

User = get_user_model()

CATEGORY_CHOICES = [('0', 'other'), ('1', 'smartphone'),  ('2', 'computers')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Product description')
    category = models.CharField(max_length=30, default='0', null=False, blank=False, choices=CATEGORY_CHOICES, verbose_name='Category')
    remainder = models.PositiveIntegerField(verbose_name='Remainder')
    price = models.DecimalField(verbose_name='Price', max_digits=7, decimal_places=2)

    def get_absolute_url(self):
        return reverse("webapp:product_view", kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price}"

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Cart(models.Model):
    product = models.ForeignKey("webapp.Product", on_delete=models.CASCADE, related_name="in_cart", verbose_name="Товар в корзине")
    qty = models.PositiveIntegerField(verbose_name='количество товара в корзине', default=1)

    def __str__(self):
        return f'{self.product.name} - {self.qty}'

    @classmethod
    def get_with_total(cls):
        return cls.objects.annotate(total=E(F("qty") * F("product__price"), output_field=models.DecimalField()))

    @classmethod
    def get_with_product(cls):
        return cls.get_with_total().select_related("product")

    @classmethod
    def get_cart_total(cls):
        total = cls.get_with_total().aggregate(cart_total=Sum("total"))
        return total['cart_total']

    class Meta:
        db_table = 'cart'
        verbose_name = 'product in cart'
        verbose_name_plural = 'products in cart'


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    address = models.CharField(max_length=100, verbose_name='Address')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    products = models.ManyToManyField('webapp.Product', related_name='orders',
                                      verbose_name='products', through='webapp.OrderProduct',
                                      through_fields=['order', 'product'])
    user = models.ForeignKey(User, related_name="orders", on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = 'Orders'


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE,
                                verbose_name='Product', related_name='order_products')
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE,
                              verbose_name='Order', related_name='order_products')
    qty = models.PositiveIntegerField(verbose_name="quantity")

    def __str__(self):
        return f'{self.product.name} - {self.order.name}'

    class Meta:
        verbose_name = 'Product in order'
        verbose_name_plural = 'products in order'
