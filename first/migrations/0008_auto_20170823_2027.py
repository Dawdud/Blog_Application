# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-23 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import first.models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(height_field='height_field', upload_to=first.models.upload_location, width_field='width_field'),
        ),
    ]