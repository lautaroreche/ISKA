from django.shortcuts import render


def home(request):
    return render(request, 'inicio.html')


def inicio(request):
    return render(request, 'inicio.html')


def servicios(request):
    return render(request, 'servicios.html')


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')


def contacto(request):
    return render(request, 'contacto.html')


def blog(request):
    return render(request, 'blog.html')
