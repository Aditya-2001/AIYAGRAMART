# Generated by Django 3.0.8 on 2020-08-20 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200817_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 20, 13, 35, 8, 636202)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 20, 13, 35, 8, 634708)),
        ),
        migrations.AlterField(
            model_name='usersorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 20, 13, 35, 8, 636848)),
        ),
    ]
