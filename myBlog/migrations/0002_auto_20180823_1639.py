# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]