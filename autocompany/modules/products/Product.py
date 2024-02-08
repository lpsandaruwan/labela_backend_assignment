import uuid

from django.db.models import Model, AutoField, UUIDField, CharField, TextField, ForeignKey, CASCADE, DecimalField

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.shared.enum.ProductCategory import ProductCategory


class Product(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=150, null=False)
    description = TextField(null=True)
    category = CharField(max_length=150, default=ProductCategory.OTHER)
    price = DecimalField(default=0, decimal_places=2, max_digits=20, null=False)
    owner = ForeignKey(AppUser, on_delete=CASCADE, null=False)

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.products'
