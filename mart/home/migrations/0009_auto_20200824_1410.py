# Generated by Django 3.0.8 on 2020-08-24 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200820_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 24, 14, 10, 32, 198904)),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 24, 14, 10, 32, 197542)),
        ),
        migrations.AlterField(
            model_name='usersorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 24, 14, 10, 32, 199494)),
        ),
    ]
