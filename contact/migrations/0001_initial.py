# Generated by Django 4.1.4 on 2022-12-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_phone', models.CharField(blank=True, max_length=15)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_message', models.TextField()),
            ],
        ),
    ]
