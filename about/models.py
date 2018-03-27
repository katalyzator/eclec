# coding=utf-8
from __future__ import unicode_literals
from geoposition.fields import GeopositionField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class AboutUS(models.Model):
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    title = models.CharField(max_length=255, verbose_name='Заголовок для текста')
    text = RichTextUploadingField(verbose_name='Текст о нас')

    partner_title = models.CharField(max_length=225, verbose_name='Текст всместо "Наши партнеры"',
                                     default='Наши партнеры')
    partner_text = models.TextField(verbose_name='Текст под заголовком "Наши партнеры"')

    image1 = models.ImageField(upload_to='images/about_us', null=True, blank=True,
                               verbose_name='Первое Изображение для слайдера - 490x300px')
    image2 = models.ImageField(upload_to='images/about_us', null=True, blank=True,
                               verbose_name='Второе Изображение для слайдера - 490x300px')
    image3 = models.ImageField(upload_to='images/about_us', null=True, blank=True,
                               verbose_name='Третье Изображение для слайдера - 490x300px')

    def __unicode__(self):
        return self.title


class Contacts(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    title = models.CharField(max_length=225, verbose_name='Название', default='Редактировать контакты')
    time = models.CharField(max_length=255, verbose_name='Режим работы')
    email = models.CharField(max_length=225, verbose_name='E-mail')
    phone = models.CharField(max_length=225, verbose_name='Телефоны')
    address = models.CharField(max_length=225, verbose_name='Адрес')
    location = GeopositionField(verbose_name='Маркер на карте', null=True, blank=True)

    def __unicode__(self):
        return self.title