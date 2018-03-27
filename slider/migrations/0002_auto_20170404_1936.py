# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryslider',
            options={'verbose_name': '\u0421\u043b\u0430\u0439\u0434 \u0433\u0430\u043b\u0435\u0440\u0435\u0438', 'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b \u0433\u0430\u043b\u0435\u0440\u0435\u0438'},
        ),
        migrations.AlterModelOptions(
            name='mainslider',
            options={'verbose_name': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439', 'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440\u044b \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439'},
        ),
        migrations.AlterModelOptions(
            name='partnerslider',
            options={'verbose_name': '\u041b\u043e\u0433\u043e \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430', 'verbose_name_plural': '\u041b\u043e\u0433\u043e\u0442\u0438\u043f\u044b \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u043e\u0432'},
        ),
        migrations.AddField(
            model_name='partnerslider',
            name='image',
            field=models.ImageField(default=1, upload_to='images/slider/partners', verbose_name='\u041b\u043e\u0433\u043e \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u043e\u0432'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partnerslider',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430'),
            preserve_default=False,
        ),
    ]
