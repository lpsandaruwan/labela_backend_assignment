import uuid

from django.db.models import Model, UUIDField, AutoField, OneToOneField, CASCADE, DecimalField

from autocompany.modules.app_users.AppUser import AppUser


class Cart(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    app_user = OneToOneField(AppUser, on_delete=CASCADE, related_name='cart_user')
    total_price = DecimalField(default=0)

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.carts'
