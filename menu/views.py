from django.shortcuts import render
from .models import Breakfast, Lunch, Dinner


# Create your views here.
def menu(request):
    breakfast = Breakfast.objects.all().filter(is_published=True)
    lunch = Lunch.objects.all().filter(is_published=True)
    dinner = Dinner.objects.all().filter(is_published=True)

    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner
    }
    return render(request, 'menu/menu.html', context)