from django.shortcuts import render
from django.views import View
from store.models import Product

class HomeView(View):
    def get(self, request):
        product_qs = Product.objects.all().filter(is_available=True)
        context = {'products': product_qs}
        return render(request, 'home.html', context)