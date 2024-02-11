from django.urls import path

from autocompany.modules.addresses.address_service import get_all_or_create, get_by_uid

urlpatterns = [
    path('addresses', get_all_or_create, name='get_all_or_create_addresses'),
    path('addresses/<str:uid>', get_by_uid, name='get_address_by_uid')
]
