from rest_framework.serializers import ModelSerializer

from autocompany.modules.addresses.Address import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['uid', 'postal_code', 'street_address', 'address_type']
