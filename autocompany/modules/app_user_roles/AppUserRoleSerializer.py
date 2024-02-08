from rest_framework.serializers import ModelSerializer

from autocompany.modules.app_user_roles.AppUserRole import AppUserRole


class AppUserRoleSerializer(ModelSerializer):
    class Meta:
        model = AppUserRole
        fields = ['uid', 'role', 'permissions']
