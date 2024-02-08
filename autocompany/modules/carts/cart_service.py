from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.carts.Cart import Cart
from autocompany.modules.carts.CartSerializer import CartSerializer
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

            carts = Cart.objects.filter(owner=app_user)
        else:
            carts = Cart.objects.all()

        serializer = CartSerializer(carts, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    except Cart.DoesNotExist:
        return JsonResponse([], status=status.HTTP_204_NO_CONTENT)


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
    app_user_uid = request.data['app_user']

    # Transform app_user uid into pk.
    if app_user_uid:
        app_user = validate_object(AppUser, app_user_uid, 'AppUser')
        if not app_user:
            return app_user
        request.data['app_user'] = app_user.id

    else:
        return JsonResponse({'error': 'Field \'app_user\' is required.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CartSerializer(data=request.data)

    if serializer.is_valid():
        cart = serializer.save()
        return JsonResponse(CartSerializer(cart).data, status=status.HTTP_201_CREATED)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
