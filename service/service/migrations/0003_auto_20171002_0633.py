# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20171002_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='amrdoc',
            name='quality',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='amrdoc',
            name='status',
            field=models.TextField(blank=True),
        ),
    ]
