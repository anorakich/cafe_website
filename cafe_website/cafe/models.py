from django.db import models
from django.urls import reverse
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


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


class Dicty(models.Model):
    name = models.CharField(max_length=50)


class KeyVal(models.Model):
    dict = models.ForeignKey(Dicty, db_index=True, on_delete=models.SET_NULL, null=True)
    key = models.IntegerField(null=True)
    value = models.IntegerField(null=True)


class Cart(models.Model):

    dishes = models.ManyToManyField(Dish)
    dishes_counter = models.OneToOneField(Dicty, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('cart', attr=[self.id])


@receiver(m2m_changed, sender=Cart.dishes.through)
def event_handler(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    pk_set = kwargs.pop('pk_set', None)
    action = kwargs.pop('action', None)
    for pk in pk_set:
        if action == 'pre_add':
            if KeyVal.objects.filter(dict=instance.dishes_counter, key=pk):
                keyval = KeyVal.objects.get(dict=instance.dishes_counter, key=pk)
                keyval.value += 1
                keyval.save()
            else:
                keyval = KeyVal.objects.create(dict=instance.dishes_counter, key=pk, value=1)
                keyval.save()
        elif action == 'pre_remove':
            cart = Cart.objects.get(id=pk)
            keyval = KeyVal.objects.get(dict=cart.dishes_counter, key=instance.id)
            if keyval.value == 1:
                keyval.delete()
            else:
                keyval.value -= 1
                keyval.save()