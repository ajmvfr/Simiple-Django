from django.shortcuts import render, redirect
from .models import Type


def home(request):

    types = Type.objects.all()

        
    context = {'types': types,
               }
    return render(request, 'main/home.html',context )