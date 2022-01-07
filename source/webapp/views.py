from django.shortcuts import render

# Create your views here.
from webapp.models import Product


def index_view(request):
    products = Product.objects.filter(remainder__gte=1).order_by('category', 'name')
    return render(request, "index.html", {'products': products})


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "product_view.html", {'product': product})

