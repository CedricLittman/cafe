# Generated by Django 3.2.18 on 2023-03-31 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_ordermodel_is_shipped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
