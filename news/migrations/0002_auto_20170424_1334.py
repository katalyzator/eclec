# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-24 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/news', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438 - 226x336px'),
        ),
    ]
