from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('product/<str:slug>/',views.ProductDetails.as_view(),name='product'),
    path('category/<str:slug>/',views.CategoryDetails.as_view(),name='category'),
    path('product-list/',views.ProductList.as_view(),name='product-list'),
    path('search-products/',views.SearchProducts.as_view(),name='search-products'),
    path('no_result/',views.NoResult,name='no_result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)