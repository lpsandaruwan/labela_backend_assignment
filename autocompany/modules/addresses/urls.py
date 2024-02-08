from django.urls import path

from autocompany.modules.addresses.address_service import get_all, get_by_uid, post

urlpatterns = [
    path('addresses', get_all, name='get_all'),
    path('addresses/<str:uid>', get_by_uid, name='get_address_by_uid'),
    path('addresses', post, name='create_address')
]
