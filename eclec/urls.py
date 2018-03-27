"""eclec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from about.views import *
from eclec import settings

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^news/$', news, name='news'),
    url(r'^news/get$', ajax_get_news, name='news_paginate'),
    url(r'^news/get/(?P<pk>[0-9]+)$', get_news, name='get_news'),
    url(r'^gallery/$', gallery, name='gallery'),
    url(r'^gallery/video$', video, name='video'),
    url(r'^gallery/image$', image, name='image'),
    url(r'^service/get/(?P<id>[0-9]+)$', get_info, name='get_service'),
    url(r'^application/send/(?P<course_id>[0-9]+)$', application, name='application'),
    url(r'^review/send/(?P<course_id>\w+)$', review, name='review'),
    url(r'^vacancy/$', vacancy, name='vacancy'),
    url(r'^vacancy/submit$', vacancy_feed, name='vacancy_feed'),
    url(r'^vacancy/thanks$', thanks, name='thnks'),
    url(r'^vacancy/detail/(?P<id>[0-9]+)$', vacancy_detail, name='vacancy_detail')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += staticfiles_urlpatterns()
