# Generated by Django 4.1.4 on 2023-01-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=100)),
                ('team_image', models.ImageField(upload_to='team_photos/%Y/%m/%d/')),
            ],
        ),
    ]
