# Generated by Django 4.1 on 2023-04-26 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_number', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=255)),
                ('email_address', models.CharField(max_length=255)),
                ('phone_number', models.PositiveBigIntegerField()),
                ('street_address1', models.CharField(max_length=255, null=True)),
                ('street_address2', models.CharField(max_length=255, null=True)),
                ('town_or_city', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('postcode', models.CharField(max_length=50)),
                ('delivery_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=25)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=25)),
                ('order_data', models.DateTimeField()),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_size', models.CharField(max_length=2)),
                ('quantity', models.PositiveIntegerField()),
                ('retailprice_total', models.DecimalField(decimal_places=2, max_digits=25)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.shipment')),
            ],
        ),
    ]
