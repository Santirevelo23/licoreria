# Generated by Django 5.0.6 on 2024-05-29 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_remove_product_description_remove_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]