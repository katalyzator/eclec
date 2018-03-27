# coding=utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=255, verbose_name='Название новости')
    image = models.ImageField(upload_to='images/news', blank=True, null=True, verbose_name='Изображение новости - 226x336px')
    text = RichTextUploadingField(verbose_name='Текст новости')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.title