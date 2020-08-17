# Generated by Django 3.0.8 on 2020-08-17 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200817_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 17, 14, 25, 24, 648162)),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 17, 14, 25, 24, 646879)),
        ),
        migrations.AddField(
            model_name='product',
            name='search_tags',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='usersorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 17, 14, 25, 24, 648777)),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 17, 14, 25, 24, 646680)),
        ),
    ]
