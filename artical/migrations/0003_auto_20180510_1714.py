# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-10 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
