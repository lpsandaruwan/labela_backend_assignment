from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.cart_items.CartItem import CartItem
from autocompany.modules.cart_items.CartItemSerializer import CartItemSerializer
from autocompany.modules.carts.Cart import Cart
from autocompany.modules.products.Product import Product
from autocompany.modules.shared.validations import validate_object


@api_view(['GET'])
def get_all(request):
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
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except CartItem.DoesNotExist:
        return JsonResponse([], status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        cart_item = CartItem.objects.get(uid=uid)
        serializer = CartItemSerializer(cart_item)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return JsonResponse({
            'Error': 'Cart item does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post(request):
    serializer = CartItemSerializer(data=request.data, many=True)
    if serializer.is_valid():
        cart_items_data = serializer.validated_data

        # Create a list to store the created cart items
        created_cart_items = []

        for cart_item_data in cart_items_data:
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
            cart_item = CartItem.objects.create(app_user=app_user, product=product, cart=cart)
            created_cart_items.append(cart_item)

        # Serialize the created cart items
        serializer = CartItemSerializer(created_cart_items, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patch_by_uid(request, uid):
    try:
        instance = CartItem.objects.get(uid=uid)
    except CartItem.DoesNotExist:
        return JsonResponse({'error': 'Cart Item does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CartItemSerializer(instance, data=request.data, partial=True)
    if serializer.is_valid():
        cart_item = serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
