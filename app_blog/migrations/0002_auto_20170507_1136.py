# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.IntegerField(verbose_name='\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='user',
            name='permission',
            field=models.IntegerField(verbose_name='\u6743\u9650'),
        ),
    ]