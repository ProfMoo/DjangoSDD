# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_quarterback'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarterback',
            name='name',
            field=models.CharField(default='yo', max_length=200),
        ),
        migrations.AddField(
            model_name='quarterback',
            name='yards',
            field=models.IntegerField(default=0),
        ),
    ]
