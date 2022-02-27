from django.contrib import admin

# Register your models here.
from webapp.models import Product, Cart, OrderProduct, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'category', 'price', 'remainder']
    list_display_links = ['pk', 'name']
    list_filter = ['category']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'category', 'price', 'remainder']


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    fields = ('product', 'qty')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'created_at')
    list_display_links = ('pk', 'name')
    ordering = ["-created_at"]
    inlines = (OrderProductInline,)


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)