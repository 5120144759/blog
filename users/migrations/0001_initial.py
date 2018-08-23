# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('icon', models.ImageField(default='', upload_to='upload')),
            ],
        ),
    ]