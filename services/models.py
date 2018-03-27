# coding=utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=225, verbose_name='Название категории')

    def __unicode__(self):
        return self.title


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    title = models.CharField(max_length=255, verbose_name='Название услуги')
    name = models.CharField(max_length=32, verbose_name='Короткое название')
    bg_image = models.ImageField(upload_to='images/service', verbose_name='Изображение фона - 215x215')
    image = models.ImageField(upload_to='images/service - 190x114')
    text = RichTextUploadingField(verbose_name='Текс услуги')
    group_size = models.CharField(max_length=150, verbose_name='Размер группы')
    duration = models.CharField(max_length=40, verbose_name='Длительность')
    time = models.CharField(max_length=20, verbose_name='Занятия')
    age = models.CharField(max_length=30, verbose_name='Возраст')
    cost = models.CharField(max_length=60, verbose_name='Стоимость')
    category = models.ForeignKey(Category, verbose_name='Категория')

    def __unicode__(self):
        return self.title


class Application(models.Model):
    class Meta:
        verbose_name = 'Завка'
        verbose_name_plural = 'Заявки'

    title = models.CharField(max_length=200, verbose_name='Название курса')
    name = models.CharField(max_length=32, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.title