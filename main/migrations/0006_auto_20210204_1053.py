# Generated by Django 3.1.4 on 2021-02-04 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_savatcha'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Maxsulot',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='savatcha',
            old_name='maxsulot',
            new_name='product',
        ),
    ]
