# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-11 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='Subjectname6',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='Subjectname7',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attsub1',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attsub2',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attsub3',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attsub4',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attsub5',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attsub6',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attsub7',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='subjectname1',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='subjectname3',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='subjectname4',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='attendance',
            name='subjectname5',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(default='', max_length=30),
        ),
    ]
