# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle', '0006_auto_20161102_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipedetails',
            old_name='description',
            new_name='recipedescription',
        ),
    ]
