from django.urls import path

from autocompany.modules.products.product_service import get_all, get_by_uid, post, patch_by_uid

urlpatterns = [
    path('products', get_all, name='get_products'),
    path('products', post, name='create_product'),
    path('products/<str:uid>', get_by_uid, name='get_product_by_uid'),
    path('products/<str:uid>', patch_by_uid, name='update_product'),
]
