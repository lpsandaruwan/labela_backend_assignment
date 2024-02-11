from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.addresses.Address import Address
from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.carts.Cart import Cart
from autocompany.modules.orders.Order import Order
from autocompany.modules.orders.OrderSerializer import OrderSerializer
from autocompany.modules.shared.validations import validate_object


def get_orders(request):
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
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def create_order(request):
    try:
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

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def get_order_by_uid(uid):
    try:
        order = Order.objects.get(uid=uid)
        serializer = OrderSerializer(order)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def patch_order_by_uid(request, uid):
    try:
        instance = Order.objects.get(uid=uid)
        serializer = OrderSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            order = serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_or_create_orders(request):
    if request.method == 'GET':
        return get_orders(request)

    elif request.method == 'POST':
        return create_order(request)


@api_view(['GET', 'PATCH'])
def get_or_update_order_by_uid(request, uid):
    if request.method == 'GET':
        return get_order_by_uid(uid)

    elif request.method == 'PATCH':
        return patch_order_by_uid(request, uid)
