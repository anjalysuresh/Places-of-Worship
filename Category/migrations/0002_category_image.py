# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-25 14:12
from __future__ import unicode_literals

import Category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=Category.models.get_file_path),
        ),
    ]