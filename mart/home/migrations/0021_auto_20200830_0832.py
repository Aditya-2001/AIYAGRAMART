# Generated by Django 3.0.8 on 2020-08-30 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200830_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 30, 8, 32, 13, 274798)),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturing_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 30, 8, 32, 13, 273503)),
        ),
        migrations.AlterField(
            model_name='usersorders',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 30, 8, 32, 13, 275393)),
        ),
    ]
