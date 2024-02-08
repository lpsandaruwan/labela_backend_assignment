from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.addresses.Address import Address
from autocompany.modules.addresses.AddressSerializer import AddressSerializer
from autocompany.modules.shared.validations import valid_app_user


@api_view(['GET'])
def get_all(request):
    addresses = []
    try:
        app_user = request.GET.get('app_user')
        if app_user:
            valid_user, result = valid_app_user(app_user)
            if valid_user:
                addresses = Address.objects.filter(owner=result['id'])
        serializer = AddressSerializer(addresses)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except Address.DoesNotExist:
        return JsonResponse(addresses, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        address = Address.objects.get(uid=uid)
        serializer = AddressSerializer(address)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except Address.DoesNotExist:
        return JsonResponse({
            'Error': 'Address does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post(request):
    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        address = serializer.save()
        return JsonResponse(AddressSerializer(address).data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
