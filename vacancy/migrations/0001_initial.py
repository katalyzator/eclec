# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-29 12:50
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0438')),
                ('salary', models.CharField(max_length=255, verbose_name='\u0412\u043f\u0438\u0448\u0438\u0442\u0435 \u0433\u0440\u0430\u0444\u0438\u043a \u0440\u0430\u0431\u043e\u0442\u044b \u0438 \u0437\u0430\u0440\u0430\u0431\u043e\u0442\u043d\u0443\u044e \u043f\u043b\u0430\u0442\u0443')),
                ('short_description', models.TextField(max_length=500, verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0438')),
                ('basic', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0411\u0430\u0437\u043e\u0432\u044b\u0435 \u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('conditions', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041e\u0431\u0449\u0438\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u044f',
                'verbose_name_plural': '\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='VacancyFeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f \u0438 \u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('file', models.FileField(upload_to='documents/', verbose_name='\u0420\u0435\u0437\u044e\u043c\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.Vacancy', verbose_name='\u0412\u0430\u043a\u0430\u043d\u0441\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041e\u0442\u043a\u043b\u0438\u043a \u043d\u0430 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u044e',
                'verbose_name_plural': '\u041e\u0442\u043a\u043b\u0438\u043a\u0438 \u043d\u0430 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u044e',
            },
        ),
    ]
