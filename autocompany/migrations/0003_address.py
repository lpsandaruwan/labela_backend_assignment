# Generated by Django 5.0 on 2024-02-08 12:34

import autocompany.modules.shared.enum.AddressType
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocompany', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('postal_code', models.TextField(max_length=10)),
                ('street_address', models.TextField()),
                ('address_type', models.CharField(default='shipping', verbose_name=autocompany.modules.shared.enum.AddressType.AddressType)),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_user', to='autocompany.appuser')),
            ],
            options={
                'db_table': 'autocompany.addresses',
            },
        ),
    ]
