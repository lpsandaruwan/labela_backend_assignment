import uuid

from django.contrib.postgres.fields import ArrayField
from django.db.models import Model, CharField, UUIDField, AutoField

from autocompany.modules.shared.enum.AppUserType import AppUserType


class AppUserRole(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    role = CharField(max_length=50, null=False, blank=False, default=AppUserType.GUEST_USER.value)
    permissions = ArrayField(CharField(max_length=10, null=False, blank=False))

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.app_user_roles'
