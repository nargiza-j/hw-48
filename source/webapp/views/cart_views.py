from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView

from webapp.forms import AddToCartForm
from webapp.models import Product, Cart


class CartCreate(CreateView):
    model = Cart
    form_class = AddToCartForm
    template_name = 'cart/cart_create.html'

    def get_context_data(self, **kwargs):
        context = super(CartCreate, self).get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(pk=self.get_object(), **self.get_form_kwargs())

    def form_valid(self, form):
        product = self.get_object()
        cart = form.save(commit=False)
        if product not in cart:
            if product.remainder == 0:
                return "no product left"
            else:
                cart.product = product
                cart.qty = 1
                print(cart, cart.qty)
        else:
            cart.product = product
            cart.qty += 1
            print(cart.qty)
            if cart.qty >= product.remainder:
                cart.qty = product.remainder
        cart.save()
        return redirect('index')

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs.get('pk'))
