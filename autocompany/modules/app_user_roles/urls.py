from django.urls import path

from autocompany.modules.app_user_roles.app_user_role_service import get_all, get_by_uid

urlpatterns = [
    path('app_user_roles', get_all, name='get_user_roles'),
    path('app_user_roles/<str:uid>', get_by_uid, name='get_user_role_by_uid')
]
