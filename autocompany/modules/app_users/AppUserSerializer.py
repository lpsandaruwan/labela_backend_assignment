from rest_framework.serializers import ModelSerializer

from autocompany.modules.app_users.AppUser import AppUser


class AppUserSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['uid', 'name', 'email']
