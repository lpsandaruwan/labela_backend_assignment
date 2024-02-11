from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.products.Product import Product
from autocompany.modules.products.ProductSerializer import ProductSerializer
from autocompany.modules.shared.validations import validate_object


def get_products(request):
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

        # Pagination
        page = request.GET.get('page')

        per_page = request.GET.get('per_page')
        if not per_page:
            per_page = 20
        paginator = Paginator(products, per_page)

        try:
            paginator = Paginator(products, per_page)
            paginated_products = paginator.page(page)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            paginated_products = paginator.page(1)

        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            paginated_products = paginator.page(paginator.num_pages)

        serializer = ProductSerializer(paginated_products, many=True)

        # Page meta information
        page_meta = {
            'total_items': paginator.count,
            'per_page': per_page,
            'page_index': paginated_products.number,
            'has_next': paginated_products.has_next(),
            'has_previous': paginated_products.has_previous(),
            'total_pages': paginator.num_pages,
        }
        response_data = {
            'products': serializer.data,
            'page_meta': page_meta
        }

        return JsonResponse(response_data, safe=False, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def create_product(request):
    try:
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

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def get_product_by_uid(uid):
    try:
        product = Product.objects.get(uid=uid)
        serializer = ProductSerializer(product)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


def update_product_by_uid(request, uid):
    try:
        instance = Product.objects.get(uid=uid)
        serializer = ProductSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            product = serializer.save()

            return JsonResponse(ProductSerializer(product).data, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return JsonResponse({
            'Error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_or_create_products(request):
    if request.method == 'GET':
        return get_products(request)

    elif request.method == 'POST':
        return create_product(request)


@api_view(['GET', 'PATCH'])
def get_or_update_product_by_uid(request, uid):
    if request.method == 'GET':
        return get_product_by_uid(uid)

    elif request.method == 'PATCH':
        return update_product_by_uid(request, uid)
