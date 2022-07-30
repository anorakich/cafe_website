# Generated by Django 4.0.2 on 2022-07-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название ингредиента')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Названия блюда')),
                ('description', models.CharField(max_length=150, verbose_name='Описание блюда')),
                ('ingredients', models.ManyToManyField(null=True, to='cafe.Ingredient')),
            ],
        ),
    ]
