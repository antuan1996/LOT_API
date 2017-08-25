# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 12:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_created_date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('lot_name', models.CharField(max_length=50, verbose_name='Название лот')),
                ('lot_price', models.BigIntegerField(default=100, verbose_name='Цена')),
                ('lot_price_step', models.IntegerField(verbose_name='Шаг цены')),
                ('lot_last_bet', models.IntegerField(verbose_name='Ставка')),
                ('lot_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
        ),
    ]
