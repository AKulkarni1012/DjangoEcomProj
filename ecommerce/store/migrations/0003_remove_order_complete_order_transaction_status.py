# Generated by Django 4.2 on 2023-04-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
