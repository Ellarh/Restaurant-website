# Generated by Django 4.1.4 on 2022-12-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_news_news_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
        ),
    ]
