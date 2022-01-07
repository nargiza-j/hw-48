from django.shortcuts import render

# Create your views here.
from webapp.models import Product


def index_view(request):
    products = Product.objects.filter(remainder__gte=1).order_by('category', 'name')
    return render(request, "index.html", {'products': products})
