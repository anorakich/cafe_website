# Generated by Django 4.0.6 on 2022-07-30 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Dicty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название кухни')),
            ],
        ),
        migrations.CreateModel(
            name='KeyVal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
                ('dict', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.dicty')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Названия блюда')),
                ('description', models.CharField(max_length=200, verbose_name='Описание блюда')),
                ('image', models.ImageField(default='default.png', upload_to='images', verbose_name='Картинка')),
                ('price', models.IntegerField(null=True, verbose_name='Цена')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.category')),
                ('kitchen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.kitchen')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishes', models.ManyToManyField(to='cafe.dish')),
                ('dishes_counter', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.dicty')),
            ],
        ),
    ]
