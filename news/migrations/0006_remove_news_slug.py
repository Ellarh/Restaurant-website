# Generated by Django 4.1.4 on 2022-12-14 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]