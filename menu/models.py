from django.db import models


# Create your models here.
class Breakfast(models.Model):
    title = models.CharField(max_length=100)
    food_category = models.CharField(max_length=50, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    review_number = models.IntegerField()
    is_published = models.BooleanField(blank=True)
    is_special_menu = models.BooleanField(blank=True)
    def __str__(self):
        return self.title


class Lunch(models.Model):
    title = models.CharField(max_length=100)
    food_category = models.CharField(max_length=50, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    review_number = models.IntegerField()
    is_published = models.BooleanField(blank=True)
    is_special_menu = models.BooleanField(blank=True)
    def __str__(self):
        return self.title


class Dinner(models.Model):
    title = models.CharField(max_length=100)
    food_category = models.CharField(max_length=50, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    review_number = models.IntegerField()
    is_published = models.BooleanField(blank=True)
    is_special_menu = models.BooleanField(blank=True)
    def __str__(self):
        return self.title
