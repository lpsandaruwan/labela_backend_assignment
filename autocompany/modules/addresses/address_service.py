from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.addresses.Address import Address
from autocompany.modules.addresses.AddressSerializer import AddressSerializer
from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.shared.validations import validate_object


def get_all_addresses(request):
    try:
        app_user_uid = request.GET.get('app_user')

        # If app_user UID is provided, filter addresses by app_user
        if app_user_uid:
            app_user = validate_object(AppUser, app_user_uid, 'AppUser')
            if not app_user:
                return app_user

            addresses = Address.objects.filter(owner=app_user)
        else:
            addresses = Address.objects.all()

        serializer = AddressSerializer(addresses, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def create_address(request):
    try:
        request_data = request.data
        app_user_uid = request_data['app_user']

        if app_user_uid:
            app_user = validate_object(AppUser, app_user_uid, 'AppUser')
            if not app_user:
                return app_user

            request_data['app_user'] = app_user.id

        serializer = AddressSerializer(data=request_data)

        if serializer.is_valid():
            address = serializer.save()
            return JsonResponse(AddressSerializer(address).data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_all_or_create(request):
    if request.method == 'GET':
        return get_all_addresses(request)
    elif request.method == 'POST':
        return create_address(request)


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        address = Address.objects.get(uid=uid)
        serializer = AddressSerializer(address)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
