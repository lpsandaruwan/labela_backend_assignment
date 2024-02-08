from django.urls import path

from autocompany.modules.cart_items.cart_item_service import get_all, get_by_uid, post, patch_by_uid

urlpatterns = [
    path('cartitems', get_all, name='get_cart_items'),
    path('cartitems/<str:uid>', get_by_uid, name='get_cart_item_by_uid'),
    path('cartitems', post, name='create_cart_items'),
    path('cartitems/<str:uid>', patch_by_uid, name='update_cart_item_by_uid'),
]
