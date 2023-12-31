from typing import Any
from django.shortcuts import render,redirect
from django.views import generic
from .models import(
    Category,
    Product,
    Slider,
)


# Create your views here.

class home(generic.TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update(
            {
                'featured_categories': Category.objects.filter(featured=True),
                'featured_products': Product.objects.filter(featured=True),
                'sliders': Slider.objects.filter(show=True),
            }
        )
        return context

class ProductDetails(generic.DetailView):
    model=Product
    template_name='product/product_details.html'
    slug_url_kwarg='slug'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['related']=self.get_object().related
        return context

class CategoryDetails(generic.DetailView):
    model=Category
    template_name='product/category_details.html'
    slug_url_kwarg='slug'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['products']=self.get_object().products.all()
        return context