from django.views import generic
from django.shortcuts import get_object_or_404, redirect,render

from .carts import Cart
from Product.models import Product

class AddToCart(generic.View):
    def post(self, *args, **kwargs):
        product=get_object_or_404(Product, id=kwargs.get('product_id'))
        cart=Cart(self.request)
        cart.update(product.id, 1)
        return redirect('cart')

class CartItems(generic.TemplateView):
    template_name='cart/cart.html'

    def get(self,request, *args, **kwargs):
        product_id=request.GET.get('product_id',None)
        quantity=request.GET.get('quantity',None)
        clear=request.GET.get('clear',False)
        cart=Cart(request)

        if product_id and quantity:
            cart.update(int(product_id),int(quantity))
            return redirect('cart')
        
        if clear:
            cart.clear()
            return redirect('cart')
        
        return super().get(request, *args, **kwargs)
