from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_name= models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=15, blank=True)
    contact_email = models.EmailField()
    contact_message = models.TextField()
    def __str__(self):
        return self.contact_name


class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    people = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.name
