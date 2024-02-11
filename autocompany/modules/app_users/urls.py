from django.urls import path

from autocompany.modules.app_users.app_user_service import get_or_update_app_user_by_uid, create_app_user

urlpatterns = [
    path('app_users', create_app_user, name='create_user'),
    path('app_users/<str:uid>', get_or_update_app_user_by_uid, name='get_or_update_user_by_uid'),
]
