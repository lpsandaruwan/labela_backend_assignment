from django.urls import path

from autocompany.modules.carts.cart_service import get_all, get_by_uid, post

urlpatterns = [
    path('carts', get_all, name='get_carts'),
    path('carts/<str:uid>', get_by_uid, name='get_cart_by_uid'),
    path('carts', post, name='create_cart')
]
