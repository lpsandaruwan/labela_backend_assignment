from django.http import JsonResponse
from rest_framework import status

from autocompany.modules.app_users.AppUser import AppUser


def valid_app_user(uid):
    try:
        return True, AppUser.objects.get(uid=uid)
    except AppUser.DoesNotExist:
        return False, JsonResponse({
            'Error': 'User does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)
