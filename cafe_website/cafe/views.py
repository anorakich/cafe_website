from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Kitchen, Dish, Category


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
    categories = Category.objects.all()
    context['menu'] = {
        kitchen.name: {category.name: Dish.objects.filter(kitchen__exact=kitchen, category__exact=category) for category
                       in categories} for kitchen in kitchens}
    return render(request, 'inc/menu.html', context=context)
