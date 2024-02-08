import uuid

from django.db.models import Model, CharField, UUIDField, AutoField, OneToOneField, CASCADE, ForeignKey

from autocompany.modules.app_user_roles.AppUserRole import AppUserRole


class AppUser(Model):
    id = AutoField(primary_key=True)
    uid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=150)
    email = CharField(max_length=150, null=True)
    role = ForeignKey(AppUserRole, on_delete=CASCADE, related_name='app_user_permissions', null=False)

    class Meta:
        app_label = 'autocompany'
        db_table = 'autocompany.app_users'
