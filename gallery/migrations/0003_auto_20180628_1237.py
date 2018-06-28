# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180628_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='img',
            field=models.FileField(default='null', upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='modified_url',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]