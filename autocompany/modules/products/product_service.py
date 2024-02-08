from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.products.Product import Product
from autocompany.modules.products.ProductSerializer import ProductSerializer
from autocompany.modules.shared.validations import validate_object


@api_view(['GET'])
def get_all(request):
    try:
        owner_uid = request.GET.get('owner')

        # If owner UID is provided, filter products by owner
        if owner_uid:
            owner = validate_object(AppUser, owner_uid, 'AppUser')
            if not owner:
                return owner

            products = Product.objects.filter(owner=owner)
        else:
            products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    except Product.DoesNotExist:
        return JsonResponse([], status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_by_uid(request, uid):
    try:
        product = Product.objects.get(uid=uid)
        serializer = ProductSerializer(product)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Product.DoesNotExist:
        return JsonResponse({
            'Error': 'Product does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        owner_uid = request.GET.get('owner')

        # If owner UID is provided, filter products by owner
        if owner_uid:
            owner = validate_object(AppUser, owner_uid, 'AppUser')

            if not owner:
                return owner
            product = serializer.save(owner=owner)
            return JsonResponse(ProductSerializer(product).data, status=status.HTTP_201_CREATED)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patch_by_uid(request, uid):
    try:
        instance = Product.objects.get(uid=uid)

    except Product.DoesNotExist:
        return JsonResponse({
            'Error': 'Product does not exist!'
        }, status=status.HTTP_400_BAD_REQUEST)

    serializer = ProductSerializer(instance, data=request.data, partial=True)
    if serializer.is_valid():
        product = serializer.save()

        return JsonResponse(ProductSerializer(product).data, status=status.HTTP_200_OK)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
