# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_item_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='file',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]
