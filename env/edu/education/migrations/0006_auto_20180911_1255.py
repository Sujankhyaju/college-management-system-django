# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-11 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_auto_20180911_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='subjectname',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
