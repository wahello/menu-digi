# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-22 12:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0022_restaurant_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 22, 12, 47, 58, 419489, tzinfo=utc), null=True),
        ),
    ]
