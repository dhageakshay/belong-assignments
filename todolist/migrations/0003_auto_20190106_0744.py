# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-06 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20170928_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2019-01-06'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2019-01-06'),
        ),
    ]
