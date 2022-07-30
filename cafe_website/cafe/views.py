from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def home(request):
    return render(request, 'home.html', context={})


def menuView(request, kicthen_id):
    dishes = Dish.objects.filter(kicthen__id__exact=kicthen_id)
    return render(request,)

class menuView(ListView):
    model = Dish
    template_name = 'menu.html'
    context_object_name = 'dishes'

    def get_kicthens(self):
        return Kitchen.objects.all()
