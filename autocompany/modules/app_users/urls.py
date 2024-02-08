from django.urls import path

from autocompany.modules.app_users.app_user_service import get_by_uid, post, patch_by_uid

urlpatterns = [
    path('app_users/<str:uid>', get_by_uid, name='get_user_by_uid'),
    path('app_users', post, name='create_user'),
    path('app_users', patch_by_uid, name='update_user')
]
