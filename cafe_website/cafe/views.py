from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Kitchen, Dish, Category


def home(request):
    context = {}
    kitchens = Kitchen.objects.all()
    categories = Category.objects.all()
    context['menu'] = {
        kitchen.name: {category.name: Dish.objects.filter(kitchen__exact=kitchen, category__exact=category) for category
                       in categories} for kitchen in kitchens}
    return render(request, 'inc/menu.html', context=context)
