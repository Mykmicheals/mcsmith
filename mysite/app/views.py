from django.shortcuts import render
from .models import Projects, Services


def index(request):
    projects = Projects.objects.all()
    services = Services.objects.all()
    return render(request, 'app/index.html', {'projects': projects, 'services': services})


def about(request):
    return render(request, 'app/about.html')


def service(request):
    services = Services.objects.all()
    return render(request, 'app/service.html', {'services': services})


def team(request):
    return render(request, 'app/team.html')


def project(request):
    projects = Projects.objects.all()
    return render(request, 'app/portfolio.html', {'projects': projects})


def contact(request):
    return render(request, 'app/contact.html')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
