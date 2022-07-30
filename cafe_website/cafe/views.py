from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


def session(func):
    def set_session(request, *args, **kwargs):
        if 'activated' not in request.session:
            request.session.set_expiry(1200)
            request.session['activated'] = True
        return func(request, *args, **kwargs)
    return set_session


@session
def home(request):
    context = {}
    kitchens = Kitchen.objects.all()
    context['dishes'] = {kitchen.name: Dish.objects.filter(kitchen__name__exact=kitchen.name) for kitchen in kitchens}
    return render(request, 'inc/card.html', context=context)
