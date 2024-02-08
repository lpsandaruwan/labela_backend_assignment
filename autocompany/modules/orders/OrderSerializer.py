from rest_framework.serializers import ModelSerializer

from autocompany.modules.orders.Order import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['uid', 'cart', 'status', 'app_user', 'address', 'delivery_date']
