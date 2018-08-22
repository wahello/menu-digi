# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_auto_20180821_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(choices=[(True, 'Complete'), (False, 'Incomplete')], default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]