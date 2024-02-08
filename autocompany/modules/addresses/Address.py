import uuid

from django.db.models import Model, AutoField, UUIDField, TextField, CharField, ForeignKey, CASCADE

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.shared.enum.AddressType import AddressType


class Address(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    postal_code = TextField(max_length=10, null=False)
    street_address = TextField(null=False)
    address_type = CharField(AddressType, default=AddressType.SHIPPING.value, null=False)
    app_user = ForeignKey(AppUser, on_delete=CASCADE, related_name='address_user', null=False)

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.addresses'
