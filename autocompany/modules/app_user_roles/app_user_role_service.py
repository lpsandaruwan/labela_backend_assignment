from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_user_roles.AppUserRole import AppUserRole
from autocompany.modules.app_user_roles.AppUserRoleSerializer import AppUserRoleSerializer


@api_view(['GET'])
def get_all(request):
    try:
        users = AppUserRole.objects.all()
        serializer = AppUserRoleSerializer(users, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    except AppUserRole.DoesNotExist:
        return JsonResponse([], status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        user = AppUserRole.objects.get(uid=uid)
        serializer = AppUserRoleSerializer(user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except AppUserRole.DoesNotExist:
        return JsonResponse({
            'Error': 'User role does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)
