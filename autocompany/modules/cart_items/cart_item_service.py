from django.core import exceptions
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.cart_items.CartItem import CartItem
from autocompany.modules.cart_items.CartItemSerializer import CartItemSerializer
from autocompany.modules.carts.Cart import Cart
from autocompany.modules.products.Product import Product
from autocompany.modules.shared.validations import validate_object


def update_cart(cart_id, amount):
    cart_instance = Cart.objects.get(id=cart_id)
    cart_instance.total_price += amount
    cart_instance.save()


def get_all_cart_items(request):
    try:
        cart_uid = request.GET.get('cart')

        # If cart UID is provided, filter cart items by cart
        if cart_uid:
            cart = validate_object(Cart, cart_uid, 'Cart')
            if not cart:
                return cart

            cart_items = CartItem.objects.filter(cart=cart)
        else:
            cart_items = CartItem.objects.all()

        serializer = CartItemSerializer(cart_items, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def create_cart_item(request):
    try:
        cart_item_data = request.data
        app_user = validate_object(AppUser, cart_item_data['app_user'], 'User')
        if not app_user:
            return app_user

        product = validate_object(Product, cart_item_data['product'], 'Product')
        if not product:
            return product

        cart = validate_object(Cart, cart_item_data['cart'], 'Cart')
        if not cart:
            return cart

        # Create the cart item and append it to the list of created cart items
        cart_item_data['product'] = product.id
        cart_item_data['app_user'] = app_user.id
        cart_item_data['cart'] = cart.id

        serializer = CartItemSerializer(data=cart_item_data)
        if serializer.is_valid():
            cart_item = serializer.save()

            amount = product.price * cart_item.quantity
            update_cart(cart.id, amount)

            return JsonResponse(CartItemSerializer(cart_item).data, safe=False, status=status.HTTP_201_CREATED)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def get_cart_item_by_uid(uid):
    try:
        cart_item = CartItem.objects.get(uid=uid)
        serializer = CartItemSerializer(cart_item)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def patch_cart_item_by_uid(request, uid):
    try:
        instance = CartItem.objects.get(uid=uid)
        serializer = CartItemSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            cart_item = serializer.save()
            instance = CartItem.objects.select_related('product', 'app_user', 'cart').get(uid=uid)

            amount = instance.product.price * instance.quantity
            update_cart(instance.cart.id, amount)

            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def delete_cart_item_by_uid(uid):
    try:
        instance = CartItem.objects.select_related('product', 'app_user', 'cart').get(uid=uid)

        amount = instance.product.price * instance.quantity
        update_cart(instance.cart.id, -amount)

        instance.delete()

        return JsonResponse({'message': 'Cart Item successfully deleted!'}, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_or_create_cart_items(request):
    if request.method == 'GET':
        return get_all_cart_items(request)

    if request.method == 'POST':
        return create_cart_item(request)


@api_view(['GET', 'DELETE', 'PATCH'])
def get_or_patch_or_delete_cart_item_by_uid(request, uid):
    if request.method == 'GET':
        return get_cart_item_by_uid(uid)

    elif request.method == 'DELETE':
        return delete_cart_item_by_uid(uid)

    elif request.method == 'PATCH':
        return patch_cart_item_by_uid(request, uid)
