# Generated by Django 4.1 on 2023-12-08 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update_data',
            new_name='update_date',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='created_data',
            new_name='created_date',
        ),
    ]
