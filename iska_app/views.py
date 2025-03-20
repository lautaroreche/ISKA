from django.shortcuts import render
from .models import Carousel, Service, Faq, Team, Post
from .forms import ContactForm
from django.http import HttpResponse


def inicio(request):
    images_carousel = Carousel.objects.all()
    services = Service.objects.all()
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
    services_key_words = {}
    services = Service.objects.all()
    for service in services:
        services_key_words[service] = service.key_words.split(',')
    context = {
        'services': services,
        'services_key_words': services_key_words,
    }
    return render(request, 'servicios.html', context)


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            return HttpResponse(f"Gracias {name}, tu mensaje ha sido enviado.")
        else:
            return render(request, 'contacto.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contacto.html', {'form': form})


def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)


def post(request, post_id):
    post = Post.objects.filter(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)
