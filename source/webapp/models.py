from django.db import models

# Create your models here.
from django.urls import reverse

CATEGORY_CHOICES = [('0', 'other'), ('1', 'smartphone'),  ('2', 'computers')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Product description')
    category = models.CharField(max_length=30, default='0', null=False, blank=False, choices=CATEGORY_CHOICES, verbose_name='Category')
    remainder = models.PositiveIntegerField(verbose_name='Remainder')
    price = models.DecimalField(verbose_name='Price', max_digits=7, decimal_places=2)

    def get_absolute_url(self):
        return reverse("product_view", kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price}"

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'

