from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_user_roles.AppUserRole import AppUserRole
from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.app_users.AppUserSerializer import AppUserSerializer
from autocompany.modules.shared.validations import validate_object


def get_app_user_by_uid(uid):
    try:
        user = AppUser.objects.get(uid=uid)
        serializer = AppUserSerializer(user)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def patch_app_user_by_uid(request, uid):
    try:
        instance = AppUser.objects.get(uid=uid)
        serializer = AppUserSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse(AppUserSerializer(user).data, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'PUT'])
def get_or_update_app_user_by_uid(request, uid):
    if request.method == 'GET':
        return get_app_user_by_uid(uid)

    if request.method == 'PATCH' or request.method == 'PUT':
        return patch_app_user_by_uid(request, uid)


@api_view(['POST'])
def create_app_user(request):
    try:
        app_user_role = validate_object(AppUserRole, request.data['role'], 'AppUserRole')

        # Validate and map role pk to app user object.
        if not app_user_role:
            return app_user_role
        request.data['role'] = app_user_role.id

        serializer = AppUserSerializer(data=request.data)

        if serializer.is_valid():
            app_user = serializer.save()
            return JsonResponse(AppUserSerializer(app_user).data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
