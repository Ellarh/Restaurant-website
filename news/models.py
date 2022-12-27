from django.db import models
from datetime import datetime

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    news_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    news_content = models.TextField(blank=True)
    date_published = models.DateField(default=datetime.now, blank=True)
    is_published = models.BooleanField(blank=True)
    is_latest = models.BooleanField(blank=True, default=True)
    def __str__(self):
        return self.title
