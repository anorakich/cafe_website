from django.shortcuts import render
from django.views.generic import ListView
from .models import *

def home(request):
    return render(request, 'home.html', context={})


class menuView(ListView):
    model = Dish
    template_name = 'menu.html'
    context_object_name = 'dishes'