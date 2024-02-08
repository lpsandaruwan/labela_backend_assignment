from rest_framework.serializers import ModelSerializer

from autocompany.modules.products.Product import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['uid', 'name', 'description', 'category', 'price']
