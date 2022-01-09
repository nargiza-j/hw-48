from django.shortcuts import render, redirect

# Create your views here.
from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request):
    products = Product.objects.filter(remainder__gte=1).order_by('category', 'name')
    return render(request, "index.html", {'products': products})


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "product_view.html", {'product': product})


def create_product_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_create.html', {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            new_product = form.save()
            return redirect('product_view', pk=new_product.pk)
        return render(request, 'product_create.html', {"form": form})

