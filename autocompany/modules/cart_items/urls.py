from django.urls import path

from autocompany.modules.cart_items.cart_item_service import (get_or_create_cart_items,
                                                              get_or_patch_or_delete_cart_item_by_uid)

urlpatterns = [
    path('cartitems', get_or_create_cart_items, name='get_or_create_cart_items'),
    path('cartitems/<str:uid>', get_or_patch_or_delete_cart_item_by_uid, name='get_cart_item_by_uid'),
]
