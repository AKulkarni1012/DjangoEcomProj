# Generated by Django 4.2 on 2023-04-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_countrycode_shippingaddress_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='countrycode',
            field=models.CharField(max_length=2, null=True, verbose_name='+'),
        ),
    ]
