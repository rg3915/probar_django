# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-19 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_foo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foo',
            name='_id',
            field=models.AutoField(db_column='_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='_id',
            field=models.AutoField(db_column='_id', primary_key=True, serialize=False),
        ),
    ]