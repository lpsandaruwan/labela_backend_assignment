import uuid

from django.db import migrations

from autocompany.modules.shared.enum.AppUserType import AppUserType
from autocompany.modules.shared.enum.ProductCategory import ProductCategory


def enrich_test_data(apps, schema_editor):
    app_user_role = apps.get_model('autocompany', 'AppUserRole')

    # Add data to the AppUserRole model.
    # TODO: Permission based operations are not available yet.
    app_user_role.objects.create(uid=uuid.uuid4(), role=AppUserType.ADMIN_USER.value, permissions=['*'])
    app_user_role.objects.create(uid=uuid.uuid4(), role=AppUserType.GUEST_USER.value, permissions=['read.*'])
    product_owner_role = app_user_role.objects.create(uid=uuid.uuid4(), role=AppUserType.PRODUCT_OWNER.value,
                                                      permissions=['*'])
    app_user_role.objects.create(uid=uuid.uuid4(), role=AppUserType.CUSTOMER.value, permissions=['*'])

    # Add product owners test data.
    app_user = apps.get_model('autocompany', 'AppUser')
    product_owner = app_user.objects.create(uid=uuid.uuid4(), role=product_owner_role, name='Product Owner',
                                            email='pown@po.com')

    # Enrich test products.
    product = apps.get_model('autocompany', 'Product')
    product.objects.create(uid=uuid.uuid4(), name='Bosch ECU', description='Matured product', price=300.99,
                           category=ProductCategory.POWER_TRAIN, owner=product_owner)
    product.objects.create(uid=uuid.uuid4(), name='MICHELIN Pilot',
                           description='Designed to provide steering precision, ultra-grip.', price=99.99,
                           category=ProductCategory.TIRES, owner=product_owner)
    product.objects.create(uid=uuid.uuid4(), name='Dorman exhaust manifold',
                           description='Improvement in your vehicle\'s performance.', price=199.99,
                           category=ProductCategory.EXHAUST_SYSTEM, owner=product_owner)


class Migration(migrations.Migration):
    dependencies = [
        ('autocompany', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(enrich_test_data),
    ]
