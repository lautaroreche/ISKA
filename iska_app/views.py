from django.shortcuts import render
from .models import Carousel, Services, Faq, Team


def inicio(request):
    images_carousel = Carousel.objects.all()
    services = Services.objects.all()
    faqs = Faq.objects.all()
    team = Team.objects.all()
    context = {
        'images_carousel': images_carousel,
        'services': services,
        'faqs': faqs,
        'team': team,
    }
    return render(request, 'inicio.html', context)


def servicios(request):
    return render(request, 'servicios.html')


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')


def contacto(request):
    return render(request, 'contacto.html')


def blog(request):
    return render(request, 'blog.html')
