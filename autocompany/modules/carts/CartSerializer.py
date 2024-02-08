from rest_framework.serializers import ModelSerializer

from autocompany.modules.carts.Cart import Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['uid', 'total_price']
