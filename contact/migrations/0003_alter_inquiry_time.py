# Generated by Django 4.1.4 on 2022-12-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
