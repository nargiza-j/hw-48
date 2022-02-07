from django import forms
from django.forms import widgets

from webapp.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=0)

