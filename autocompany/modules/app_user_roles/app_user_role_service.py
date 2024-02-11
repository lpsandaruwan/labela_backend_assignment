from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_user_roles.AppUserRole import AppUserRole
from autocompany.modules.app_user_roles.AppUserRoleSerializer import AppUserRoleSerializer


@api_view(['GET'])
def get_all(request):
    print(request)
    try:
        users = AppUserRole.objects.all()
        serializer = AppUserRoleSerializer(users, many=True)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        user = AppUserRole.objects.get(uid=uid)
        serializer = AppUserRoleSerializer(user)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
