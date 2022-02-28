from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView

from webapp.forms import CartForm, OrderForm
from webapp.models import Product, Cart, Order, OrderProduct


class CartCreate(CreateView):
    model = Cart
    form_class = CartForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        qty = form.cleaned_data.get('qty', 1)
        try:
            cart_product = Cart.objects.get(product=product)
            if cart_product.qty + qty <= product.remainder:
                cart_product.qty += qty
                cart_product.save()
        except Cart.DoesNotExist:
            if qty <= product.remainder:
                Cart.objects.create(product=product, qty=qty)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next = self.request.GET.get("next")
        if next:
            return next
        return reverse("webapp:index")


class CartView(ListView):
    # model = Cart
    template_name = "cart/cart_view.html"
    context_object_name = "cart"

    def get_queryset(self):
        return Cart.get_with_product()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["total"] = Cart.get_cart_total()
        context["form"] = OrderForm()
        return context


class CartDeleteView(DeleteView):
    model = Cart
    success_url = reverse_lazy("webapp:cart_view")

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CartDeleteOneView(DeleteView):
    model = Cart
    success_url = reverse_lazy("webapp:cart_view")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.qty -= 1
        if self.object.qty < 1:
            self.object.delete()
        else:
            self.object.save()
        return HttpResponseRedirect(success_url)


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("webapp:index")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        response = super().form_valid(form)
        order = self.object

        cart_products = Cart.objects.all()
        products = []
        order_products = []
        for item in cart_products:
            product = item.product
            qty = item.qty
            product.remainder -= qty
            products.append(product)
            order_product = OrderProduct(product=product, qty=qty, order=order)
            order_products.append(order_product)
        OrderProduct.objects.bulk_create(order_products)
        Product.objects.bulk_update(products, ("remainder",))
        cart_products.delete()
        return response


class OrdersView(LoginRequiredMixin, ListView):
    template_name = "cart/order_view.html"
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
