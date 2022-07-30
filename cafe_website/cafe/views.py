from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def home(request):
    context = {}
    kitchens = Kitchen.objects.all()
    context['dishes'] = {kitchen.name: Dish.objects.filter(kitchen__name__exact=kitchen.name) for kitchen in kitchens}
    return render(request, 'inc/card.html', context=context)
