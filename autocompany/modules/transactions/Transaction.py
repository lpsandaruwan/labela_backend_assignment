import uuid

from django.db.models import Model, AutoField, ForeignKey, CASCADE, CharField, DecimalField
from django.forms import UUIDField

from autocompany.modules.app_users.AppUser import AppUser
from autocompany.modules.orders.Order import Order
from autocompany.modules.shared.enum.TransactionStatus import TransactionStatus
from autocompany.modules.shared.enum.TransactionType import TransactionType


class Transaction(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    order = ForeignKey(Order, on_delete=CASCADE, related_name='transaction_order', null=False)
    user = ForeignKey(AppUser, on_delete=CASCADE, related_name='transaction_user', null=False)
    type = CharField(max_length=20, default=TransactionType.CHARGE.value)
    status = CharField(max_length=20, default=TransactionStatus.IN_PROGRESS.value)
    amount = DecimalField(null=False)

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.transactions'
