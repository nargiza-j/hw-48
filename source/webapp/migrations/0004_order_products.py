# Generated by Django 4.0.1 on 2022-02-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_order_alter_cart_product_alter_cart_qty_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='webapp.OrderProduct', to='webapp.Product', verbose_name='products'),
        ),
    ]
