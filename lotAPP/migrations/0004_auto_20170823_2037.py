# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotAPP', '0003_auto_20170823_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='lot_name',
            field=models.CharField(max_length=50, verbose_name='Название лота'),
        ),
    ]
