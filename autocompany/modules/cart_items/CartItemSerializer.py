from rest_framework.serializers import ModelSerializer

from autocompany.modules.cart_items.CartItem import CartItem


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['uid', 'cart', 'quantity', 'app_user', 'product']
