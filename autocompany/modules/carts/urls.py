from django.urls import path

from autocompany.modules.carts.cart_service import get_or_create_carts, get_cart_by_uid

urlpatterns = [
    path('carts', get_or_create_carts, name='get_or_create_carts'),
    path('carts/<str:uid>', get_cart_by_uid, name='get_cart_by_uid'),
]
