# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-04 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youth', '0002_auto_20190804_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youthdetails',
            name='married',
            field=models.CharField(max_length=100),
        ),
    ]