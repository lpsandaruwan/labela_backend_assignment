from django.urls import path

from autocompany.modules.orders.order_service import get_all, get_by_uid, post, patch_by_uid

urlpatterns = [
    path('orders', get_all, name='get_orders'),
    path('orders/get/<str:uid>', get_by_uid, name='get_order_by_uid'),
    path('orders/create', post, name='create_order'),
    path('orders/update/<str:uid>', patch_by_uid, name='update_by_uid'),
]
