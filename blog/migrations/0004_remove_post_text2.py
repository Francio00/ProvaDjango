# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text2',
        ),
    ]