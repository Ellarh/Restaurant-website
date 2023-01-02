from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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


def detail(request, detail_id):
    news = get_object_or_404(News,id=detail_id)

    context = {
        'news': news
    }
    return reverse(request, 'news/news_detail.html', context)
