# Generated by Django 4.1 on 2023-12-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_category_slug_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]