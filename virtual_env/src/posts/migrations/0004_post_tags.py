# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-25 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django_postgres_extensions.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190225_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=django_postgres_extensions.models.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, form_size=None, null=True, size=None),
        ),
    ]