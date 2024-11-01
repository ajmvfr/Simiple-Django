from django.shortcuts import render, redirect
from .models import Type


def home(request):
    url = request.build_absolute_uri()
    root_url = url.split('/')[2]

    types = Type.objects.all()
        
    context = {'types': types,
               'root' : root_url
               }
    return render(request, 'main/home.html',context )