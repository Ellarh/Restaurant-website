from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):
    news = News.objects.all().filter(is_published=True)
    latest_news = News.objects.all().filter(is_latest=True)

    context = {
        'news': news,
        'latest_news': latest_news
    }
    return render(request, 'news/news.html', context)


def detail(request):
    news = News.objects.all().filter(is_published=True)

    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)
