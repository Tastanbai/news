# news/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Tag

def news_list(request):
    news_list = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_list, 10) # показывать по 10 новостей на странице
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.views_count += 1
    news.save()
    return render(request, 'news/news_detail.html', {'news': news})
# news/views.py


def news_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    news_list = tag.news.all().order_by('-created_at')
    paginator = Paginator(news_list, 10)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    return render(request, 'news/news_by_tag.html', {'news': news, 'tag': tag})


def news_statistics(request):
    news_statistics = News.objects.all().order_by('-views_count')
    return render(request, 'news/news_statistics.html', {'news_statistics': news_statistics})
