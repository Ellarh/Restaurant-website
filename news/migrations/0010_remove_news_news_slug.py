# Generated by Django 4.1.4 on 2022-12-25 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_news_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_slug',
        ),
    ]
