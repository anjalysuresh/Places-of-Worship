# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-05 07:03
from __future__ import unicode_literals

import Course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0010_topicarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to=Course.models.get_file_path),
        ),
    ]