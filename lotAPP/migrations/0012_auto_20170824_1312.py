# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotAPP', '0011_lot_lot_bool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='lot_bool',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
    ]
