# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isComplete',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
