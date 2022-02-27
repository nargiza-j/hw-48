# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product
from webapp.views.base import SearchView


class ProductList(SearchView):
    model = Product
    template_name = "products/index.html"
    context_object_name = "products"
    paginate_by = 5
    search_fields = ["name__icontains", "description__icontains", "category__icontains"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(remainder__gte=1).order_by('category', 'name')


class ProductView(DetailView):
    model = Product
    template_name = "products/product_view.html"


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update.html'


class ProductDelete(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy('webapp:index')
