# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class MainSlider(models.Model):
    class Meta:
        verbose_name = 'Слайдер на главной'
        verbose_name_plural = 'Слайдеры на главной'

    title = models.CharField(max_length=255, verbose_name='Название слайда', null=True, blank=True)
    text = models.TextField(verbose_name='Текст слайдера', null=True, blank=True)
    image = models.ImageField(upload_to='images/slider/main', verbose_name='Изображение слайдера 1300x390px', null=True, blank=True)

    def __unicode__(self):
        return self.title


class GallerySlider(models.Model):
    class Meta:
        verbose_name = 'Слайд галереи'
        verbose_name_plural = 'Слайды галереи'

    title = models.CharField(max_length=225, verbose_name='Название слайда')
    image = models.ImageField(upload_to='images/slider/gallery', verbose_name='Изображение слайдера - пропорции 1х1', null=True, blank=True)
    video = models.CharField(max_length=225, verbose_name='Cсылка видео с youtube', null=True, blank=True)
    video_image = models.CharField(max_length=225, verbose_name='Cпециальные артикул youtube', null=True, blank=True)

    def __unicode__(self):
        return self.title


class PartnerSlider(models.Model):
    class Meta:
        verbose_name = 'Лого партнера'
        verbose_name_plural = 'Логотипы партнеров'

    title = models.CharField(max_length=255, verbose_name='Название партнера')
    image = models.ImageField(upload_to='images/slider/partners', verbose_name='Лого партнеров - 103x103px максимально')

    def __unicode__(self):
        return self.title


class ForeingSlider(models.Model):
    class Meta:
        verbose_name = 'Слайдер отправки за рубеж'
        verbose_name_plural = 'Слайдеры отправки за рубеж'

    title = models.CharField(max_length=225, verbose_name='Название слайдера', null=True, blank=True)
    image = models.ImageField(upload_to='images/slider/parners', verbose_name='Название слайдера', null=True, blank=True)
    text = models.TextField(max_length=1000, verbose_name='Текст для слайдера', null=True, blank=True)

    def __unicode__(self):
        return str(self.image)