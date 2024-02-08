import uuid

from django.db.models import Model, CharField, UUIDField, AutoField, CASCADE, ForeignKey

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.carts.Cart import Cart
from autocompany.modules.shared.enum.OrderStatus import OrderStatus


class Order(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    cart = ForeignKey(Cart, on_delete=CASCADE, related_name='order_cart', null=False)
    app_user = ForeignKey(AppUser, on_delete=CASCADE, related_name='order_user', null=False)
    status = CharField(max_length=20, default=OrderStatus.INITIALIZED.value)

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.orders'
