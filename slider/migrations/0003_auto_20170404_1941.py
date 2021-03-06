# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_auto_20170404_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryslider',
            name='video',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='C\u0441\u044b\u043b\u043a\u0430 \u0432\u0438\u0434\u0435\u043e \u0441 youtube'),
        ),
        migrations.AddField(
            model_name='galleryslider',
            name='video_image',
            field=models.CharField(blank=True, max_length=225, null=True, verbose_name='C\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0430\u0440\u0442\u0438\u043a\u0443\u043b youtube'),
        ),
        migrations.AlterField(
            model_name='galleryslider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/slider/gallery', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430'),
        ),
    ]
