# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 13:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Community', '0017_community_forum_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communitycreator', to=settings.AUTH_USER_MODEL),
        ),
    ]