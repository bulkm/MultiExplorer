# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceTick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=8)),
                ('exchange', models.CharField(max_length=128)),
                ('base_fiat', models.CharField(max_length=8)),
                ('date', models.DateTimeField(db_index=True)),
                ('price', models.FloatField()),
            ],
            options={
                'get_latest_by': 'date',
            },
        ),
    ]
