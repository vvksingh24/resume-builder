# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-13 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20180513_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='phone_no',
            field=models.CharField(max_length=13),
        ),
    ]
