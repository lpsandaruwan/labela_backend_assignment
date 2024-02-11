from django.urls import path

from autocompany.modules.products.product_service import get_or_create_products, get_or_update_product_by_uid

urlpatterns = [
    path('products', get_or_create_products, name='get_or_create_products'),
    path('products/<str:uid>', get_or_update_product_by_uid, name='get_or_update_product_by_uid'),
]
