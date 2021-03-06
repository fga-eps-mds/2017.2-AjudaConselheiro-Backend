# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-08 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselors', '0002_auto_20170908_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='counselor',
            name='username',
            field=models.CharField(default='username', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='counselor',
            name='first_name',
            field=models.CharField(default='NOME', max_length=40),
        ),
        migrations.AlterField(
            model_name='counselor',
            name='last_name',
            field=models.CharField(default='SOBRENOME', max_length=40),
        ),
    ]
