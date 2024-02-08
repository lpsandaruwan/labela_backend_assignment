from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.app_users.AppUserSerializer import AppUserSerializer


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        user = AppUser.objects.get(uid=uid)
        serializer = AppUserSerializer(user)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except AppUser.DoesNotExist:
        return JsonResponse({
            'Error': 'User does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post(request):
    serializer = AppUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return JsonResponse(AppUserSerializer(user).data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patch_by_uid(request, uid):
    try:
        instance = AppUser.objects.get(uid=uid)
    except AppUser.DoesNotExist:
        return JsonResponse({
            'Error': 'User does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)
    serializer = AppUserSerializer(instance, data=request.data, partial=True)
    if serializer.is_valid():
        user = serializer.save()
        return JsonResponse(AppUserSerializer(user).data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
