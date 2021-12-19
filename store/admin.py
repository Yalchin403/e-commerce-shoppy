from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'slug', 'category', 'stock', 'is_available', 'created_date', 'modified_date')


admin.site.register(Product, ProductAdmin)