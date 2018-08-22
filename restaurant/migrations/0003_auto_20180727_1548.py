# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import menu_digi.cloud_fix


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_fooditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='availability',
            field=models.BooleanField(choices=[(True, 'Available'), (False, 'Unavailable')], default=False),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=menu_digi.cloud_fix.CloudinaryFieldFix(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
