# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-22 13:48
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import menu_digi.cloud_fix


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0025_order_time_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255, null=True, unique=True)),
                ('review', models.TextField(max_length=255, null=True, unique=True)),
                ('avatar', menu_digi.cloud_fix.CloudinaryFieldFix(blank=True, max_length=255, null=True, verbose_name='image')),
            ],
        ),
        migrations.AlterField(
            model_name='foodcategory',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_category', to='restaurant.Restaurant'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='restaurant.FoodCategory'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='additional_info',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='restaurant.Restaurant'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='business_email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='table',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table', to='restaurant.Restaurant'),
        ),
        migrations.AlterField(
            model_name='table',
            name='table',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurant.Restaurant'),
        ),
    ]
