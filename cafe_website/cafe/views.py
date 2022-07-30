from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def home(request):
    context = {}
    context['kitchens'] = Kitchen.objects.all()
    for kitchen in context['kitchens']:
        context[kitchen.__str__()] = Dish.objects.filter(kitchen__name=kitchen.__str__())

    return render(request, 'home.html', context=context)

