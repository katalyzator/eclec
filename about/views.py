# coding=utf-8
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, render_to_response, redirect
from django.urls import reverse

from about.models import *
from news.models import *
from reviews.models import *
from services.models import *
from slider.models import *

# Create your views here.
from vacancy.forms import VacancyForm
from vacancy.models import Vacancy, VacancyFeedBack


def main(request):
    main_slide = MainSlider.objects.all()
    category = Category.objects.all()
    service = Service.objects.all()
    part_slide = PartnerSlider.objects.all()
    last_news = News.objects.all().order_by('-date')[:2]
    last_reviews = Review.objects.all().order_by('-date')[:2]
    about_us = AboutUS.objects.first()
    contacts = Contacts.objects.first()
    foreing = ForeingSlider.objects.all()

    params = {
        'main_slide': main_slide,
        'category': category,
        'service': service,
        'part_slide': part_slide,
        'last_news': last_news,
        'last_reviews': last_reviews,
        'about_us': about_us,
        'contacts': contacts,
        'foreing': foreing,
        'location': 'index',
    }

    return render(request, 'main/index.html', params)


def news(request):
    paginator = Paginator(News.objects.all().order_by('-date'), 4)
    _news = paginator.page(1)
    page_count = paginator.num_pages

    params = {
        'news': _news,
        'page_count': page_count,
        'location': 'news',
    }
    return render(request, 'main/news.html', params)


def ajax_get_news(request):
    paginator = Paginator(News.objects.all().order_by('-date'), 4)
    _news = paginator.page(request.GET.get('page', 1))

    return render_to_response('main/partial/news_paginate.html', {'news': _news})


def get_news(request, pk):
    one_news = News.objects.filter(id=pk).first()
    next_news = News.objects.filter(id__gt=pk).order_by('id').first()
    previous_news = News.objects.filter(id__lt=pk).order_by('id').last()

    print next_news

    params = {
        'news': one_news,
        'next': next_news,
        'previous': previous_news,
        'location': 'news',

    }
    return render(request, 'main/one-news.html', params)


def gallery(request):
    _gallery = GallerySlider.objects.all()

    params = {
        'gallery': _gallery,
        'location': 'gallery',
    }

    return render(request, 'main/gallery.html', params)


def video(request):
    _video = GallerySlider.objects.all()

    params = {
        'gallery': _video,
        'location': 'video',
    }

    return render(request, 'main/video.html', params)


def image(request):
    _image = GallerySlider.objects.all()

    params = {
        'gallery': _image,
        'location': 'image',
    }

    return render(request, 'main/image.html', params)


def get_info(request, id):
    info = Service.objects.filter(id=id).first()
    reviews = Review.objects.filter(service=info)
    params = {
        'item': info,
        'reviews': reviews,
        'reviews_count': reviews.count()
    }
    return render_to_response('main/partial/modal.html', params)


def application(request, course_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        course = Service.objects.filter(id=course_id).first()
        user = Application(name=name, phone=phone, email=email, title=course.title)
        user.save()
        user_id = str(user.id)
        name = 'Моё имя: ' + str(name) + '\n'
        phone = 'Мой номер: ' + str(phone) + '\n'
        email = 'Мой email: ' + str(email) + '\n'
        send_mail('Заявка с сайта ', name + phone + email + 'Номер заявки: ' + user_id, 'asnotifications@gmail.com',
                  ['ravshan.alikovich@gmail.com'])
    return JsonResponse(dict(success=True))


def review(request, course_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        course = Service.objects.filter(id=course_id).first()
        _review = Review(name=name, text=text, service=course)
        _review.save()
        name = 'Моё имя: ' + str(name) + '\n'
        text = 'Текст отзыва: ' + str(text) + '\n'
        send_mail('Заявка с сайта ', name + text, 'asnotifications@gmail.com',
                  ['ravshan.alikovich@gmail.com'])

    return JsonResponse(dict(success=True))


def vacancy(request):
    vac = Vacancy.objects.all().order_by('-created_at')

    params = {
        'vacancies': vac,
    }
    return render(request, 'main/vacancy.html', params)


def vacancy_detail(request, id):
    one_vacancy = Vacancy.objects.get(id=id)

    params = {
        'vacancy': one_vacancy,
    }

    return render(request, 'main/vacancy_detail.html', params)


def vacancy_feed(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            vacfeed = VacancyFeedBack()
            vacfeed.vacancy = form.cleaned_data['vacancy']
            vacfeed.file = request.FILES['file']
            vacfeed.name = form.cleaned_data['name']
            vacfeed.email = form.cleaned_data['email']
            vacfeed.save()
            # messages.add_message(request, messages.INFO, 'Ваша заявка отправлена.')
            return redirect(reverse('thnks'))

    return JsonResponse(dict(success=True, message='Request is not POST!'))


def thanks(request):
    return render(request, 'main/thks.html')
