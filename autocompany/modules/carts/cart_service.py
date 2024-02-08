from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.carts.Cart import Cart
from autocompany.modules.carts.CartSerializer import CartSerializer
from autocompany.modules.shared.validations import valid_app_user


@api_view(['GET'])
def get_all(request):
    carts = []
    try:
        app_user = request.GET.get('app_user')
        if app_user:
            valid_user, result = valid_app_user(app_user)
            if valid_user:
                carts = Cart.objects.filter(owner=result['id'])
        serializer = CartSerializer(carts)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return JsonResponse(carts, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        cart = Cart.objects.get(uid=uid)
        serializer = CartSerializer(cart)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return JsonResponse({
            'Error': 'Cart does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        cart = serializer.save()
        return JsonResponse(CartSerializer(cart).data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
