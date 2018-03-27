# coding=utf-8
from __future__ import unicode_literals
from services.models import Service
from django.db import models


# Create your models here.

class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    is_active = models.BooleanField(default=False, verbose_name='Активировать')
    name = models.CharField(max_length=32, verbose_name='Имя человека')
    text = models.TextField(verbose_name='Текс отзыва')
    date = models.DateTimeField(auto_now_add=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
