import uuid

from django.db.models import Model, UUIDField, AutoField, CASCADE, ForeignKey, IntegerField

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.carts.Cart import Cart
from autocompany.modules.products.Product import Product


class CartItem(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    cart = ForeignKey(Cart, on_delete=CASCADE, related_name='cart_item', null=False)
    product = ForeignKey(Product, on_delete=CASCADE, related_name='item_product', null=False)
    app_user = ForeignKey(AppUser, on_delete=CASCADE, related_name='cart_item_user', null=False)
    quantity = IntegerField(default=0)

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.cart_items'
