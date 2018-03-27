# coding=utf-8
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class Vacancy(models.Model):
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    title = models.CharField(max_length=255, verbose_name='Название вакансии')
    salary = models.CharField(max_length=255, verbose_name='Впишите график работы и заработную плату')
    short_description = models.TextField(max_length=500, verbose_name='Короткое описание вакансии')
    basic = RichTextUploadingField(verbose_name='Базовые требования')
    conditions = RichTextUploadingField(verbose_name='Общие условия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __unicode__(self):
        return self.title


class VacancyFeedBack(models.Model):
    class Meta:
        verbose_name = 'Отклик на вакансию'
        verbose_name_plural = 'Отклики на вакансию'

    name = models.CharField(max_length=255, verbose_name='Имя и Фамилия')
    email = models.CharField(max_length=255, verbose_name='Email')
    file = models.FileField(upload_to='documents/', verbose_name='Резюме')
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __unicode__(self):
        return self.name
