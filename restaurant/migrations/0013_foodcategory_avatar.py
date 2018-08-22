# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-12 13:17
from __future__ import unicode_literals

from django.db import migrations
import menu_digi.cloud_fix


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_auto_20180812_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcategory',
            name='avatar',
            field=menu_digi.cloud_fix.CloudinaryFieldFix(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
