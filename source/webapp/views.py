from django.shortcuts import render, redirect, get_object_or_404

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


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'remainder': product.remainder,
            'price': product.price
        })
        return render(request, 'product_update.html', {"product": product, "form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.category = form.cleaned_data.get('category')
            product.remainder = form.cleaned_data.get('remainder')
            product.price = form.cleaned_data.get('price')
            product = form.save()
            return redirect('product_view', pk=product.pk)
        return render(request, 'product_update.html', {"product": product, "form": form})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, "product_delete.html", {"product": product})
    else:
        product.delete()
        return redirect("index")
