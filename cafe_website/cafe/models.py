from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название ингредиента")

    def __str__(self):
        return self.name


class Kitchen(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название кухни")

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=20, verbose_name="Названия блюда")
    description = models.CharField(max_length=150, verbose_name="Описание блюда")
    ingredients = models.ManyToManyField('Ingredient')
    kitchen = models.ForeignKey('Kitchen', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dish', attr=[str(self.id)])
