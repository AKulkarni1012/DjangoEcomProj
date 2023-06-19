# Generated by Django 4.2 on 2023-04-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_order_complete_order_transaction_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='countrycode',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
