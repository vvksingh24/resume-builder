# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-13 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20180513_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='about_you',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.TextField(),
        ),
    ]
