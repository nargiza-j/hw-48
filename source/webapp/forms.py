from django import forms
from django.forms import widgets

from webapp.models import Product, Cart, Order


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['qty']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ["products"]