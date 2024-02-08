from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.addresses.Address import Address
from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.carts.Cart import Cart
from autocompany.modules.orders.Order import Order
from autocompany.modules.orders.OrderSerializer import OrderSerializer
from autocompany.modules.shared.validations import validate_object


@api_view(['GET'])
def get_all(request):
    try:
        app_user_uid = request.GET.get('app_user')

        # If app_user UID is provided, filter carts by app_user
        if app_user_uid:
            app_user = validate_object(AppUser, app_user_uid, 'AppUser')
            if not app_user:
                return app_user

            orders = Order.objects.filter(owner=app_user)
        else:
            orders = Order.objects.all()

        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Order.DoesNotExist:
        return JsonResponse([], status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        order = Order.objects.get(uid=uid)
        serializer = OrderSerializer(order)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Order.DoesNotExist:
        return JsonResponse({
            'Error': 'Order does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post(request):
    request_data = request.data

    app_user = validate_object(AppUser, request_data['app_user'], 'AppUser')
    if not app_user:
        return app_user

    cart = validate_object(Cart, request_data['cart'], 'Cart')
    if not cart:
        return cart

    address = validate_object(Address, request_data['address'], 'Address')
    if not cart:
        return cart

    request_data['app_user'] = app_user.id
    request_data['cart'] = cart.id
    request_data['address'] = address.id

    serializer = OrderSerializer(data=request_data)
    if serializer.is_valid():
        order_data = serializer.validated_data

        order = serializer.save()
        serializer = OrderSerializer(order)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patch_by_uid(request, uid):
    try:
        instance = Order.objects.get(uid=uid)

    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = OrderSerializer(instance, data=request.data, partial=True)
    if serializer.is_valid():
        order = serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
