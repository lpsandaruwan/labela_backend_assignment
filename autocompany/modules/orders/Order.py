import uuid

from django.db.models import Model, CharField, UUIDField, AutoField, CASCADE, OneToOneField, DateField

from autocompany.modules.addresses.Address import Address
from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.carts.Cart import Cart
from autocompany.modules.shared.enum.OrderStatus import OrderStatus


class Order(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    cart = OneToOneField(Cart, on_delete=CASCADE, related_name='order_cart', null=False)
    app_user = OneToOneField(AppUser, on_delete=CASCADE, related_name='order_user', null=False)
    address = OneToOneField(Address, on_delete=CASCADE, related_name='order_shipping_address', null=True, blank=True)
    status = CharField(max_length=20, default=OrderStatus.INITIALIZED.value)
    delivery_date = DateField(null=True, blank=True)

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.orders'
