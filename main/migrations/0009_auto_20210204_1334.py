# Generated by Django 3.1.4 on 2021-02-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210204_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savatcha',
            name='quantity',
        ),
        migrations.AddField(
            model_name='savatcha',
            name='soni',
            field=models.IntegerField(default=1),
        ),
    ]
