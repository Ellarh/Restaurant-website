from django.shortcuts import render
from menu.models import Breakfast, Lunch, Dinner
from news.models import News

# Create your views here.
def index(request):
    breakfast = Breakfast.objects.all().filter(is_special_menu=True)
    lunch = Lunch.objects.all().filter(is_special_menu=True)
    dinner = Dinner.objects.all().filter(is_special_menu=True)
    latest_news = News.objects.all().filter(is_latest=True)

    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'latest_news': latest_news
    }
    return render(request, 'pages/index.html',context)


def about(request):
    return render(request, 'pages/about.html')
