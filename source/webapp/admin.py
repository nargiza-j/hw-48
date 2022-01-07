from django.contrib import admin

# Register your models here.
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'price', 'remainder']
    list_filter = ['category']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'category', 'price', 'remainder']


admin.site.register(Product, ProductAdmin)