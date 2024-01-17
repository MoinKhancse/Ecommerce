from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from django.db.models import Q
from django.core.paginator import(
    PageNotAnInteger,
    EmptyPage,InvalidPage,Paginator
)
from cart.carts import Cart

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
        context= super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().related
        return context

class CategoryDetails(generic.DetailView):
    model=Category
    template_name='product/category_details.html'
    slug_url_kwarg='slug'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['products']=self.get_object().products.all()
        return context

class CustomPaginator:
    def __init__(self,request,queryset,paginted_by) -> None:
        self.paginator=Paginator(queryset,paginted_by)
        self.paginated_by=paginted_by
        self.queryset=queryset
        self.page=request.GET.get('page',1)

    def get_queryset(self):
        try:
            queryset=self.paginator.page(self.page)
            
        except PageNotAnInteger:
            queryset=self.paginator.page(1)
        except EmptyPage:
            queryset=self.paginator.page(1)
        except InvalidPage:
            queryset=self.paginator.page(1)
            
        return queryset
        

class ProductList(generic.ListView):
    model=Product
    template_name='product/product-list.html'
    context_object_name='object_list'
    paginate_by=5

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        page_obj=CustomPaginator(self.request,self.get_queryset(),self.paginate_by)
        quryset=page_obj.get_queryset()
        paginator=page_obj.paginator
        context['object_list']=quryset
        context['paginator']=paginator
        return context

class SearchProducts(generic.View):
    def get(self,*args, **kwargs):
        key=self.request.GET.get('key','')
        products=Product.objects.filter(
            Q(title__icontains=key) |
            Q(category__title__icontains=key)
        )
        context={
            'products':products,
            "key":key
        }
        return render(self.request,'product/search-products.html',context)

      
def NoResult(request):
    return render (request,'no-result.html')  

# def Login(request):
#     return render (request,'login.html')  

# def Registration(request):
#     return render (request,'account/registration.html') 