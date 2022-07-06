from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Product
from category.models import Category
from django.shortcuts import get_object_or_404


class StoreView(View):
    def get(self, request, category_slug=None):
        if category_slug != None:
            category_qs = Category.objects.all()
            category = get_object_or_404(Category, slug=category_slug)
            product_qs = Product.objects.filter(category=category, is_available=True)

        else:
            product_qs = Product.objects.all().filter(is_available=True)
            category_qs = Category.objects.all()
        
        context = {
            'products': product_qs,
            'categories': category_qs
        }
        return render(request, 'store/store.html', context)


class ProductDetailView(View):
    def get(self, request, category_slug, product_slug):
        product_obj = get_object_or_404(Product, slug=product_slug, category__slug=category_slug)
        context = {"product": product_obj}
        
        return render(request, 'store/product_detail.html', context)