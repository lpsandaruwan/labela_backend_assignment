# Generated by Django 5.0 on 2024-02-08 12:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocompany', '0003_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('app_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart_user', to='autocompany.appuser')),
            ],
            options={
                'db_table': 'autocompany.carts',
            },
        ),
    ]