from django.urls import path
from . import views


app_name='store'
urlpatterns = [
    path('', views.StoreView.as_view(), name='home'),
    path('<slug:category_slug>/', views.StoreView.as_view(), name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    ]