from django.urls import path

from autocompany.modules.orders.order_service import get_or_create_orders, get_or_update_order_by_uid

urlpatterns = [
    path('orders', get_or_create_orders, name='get_or_create_orders'),
    path('orders/<str:uid>', get_or_update_order_by_uid, name='get_or_update_order_by_uid'),
]
