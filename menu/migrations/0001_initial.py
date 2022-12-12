# Generated by Django 4.1.4 on 2022-12-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('food_category', models.CharField(default=True, max_length=50)),
                ('new_price', models.FloatField()),
                ('old_price', models.FloatField(blank=True)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('review_number', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('is_special_menu', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('food_category', models.CharField(default=True, max_length=50)),
                ('new_price', models.FloatField()),
                ('old_price', models.FloatField(blank=True)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('review_number', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('is_special_menu', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('food_category', models.CharField(default=True, max_length=50)),
                ('new_price', models.FloatField()),
                ('old_price', models.FloatField(blank=True)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('review_number', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('is_special_menu', models.BooleanField(default=True)),
            ],
        ),
    ]