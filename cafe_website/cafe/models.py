from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Категория")

    def __str__(self):
        return self.name


class Kitchen(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название кухни")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dish', attr=[str(self.id)])


class Dish(models.Model):
    name = models.CharField(max_length=20, verbose_name="Названия блюда")
    description = models.CharField(max_length=200, verbose_name="Описание блюда")
    image = models.ImageField(upload_to="images", verbose_name="Картинка", default="default.png")
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    kitchen = models.ForeignKey('Kitchen', null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(verbose_name="Цена", null=True)

    def __str__(self):
        return self.name
