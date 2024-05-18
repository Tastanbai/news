# news/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, Tag
from django.http import JsonResponse

def news_list(request):
    news_list = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_list, 3)  # Показывать по 3 новости на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        news_data = []
        for news in page_obj:
            news_data.append({
                'title': news.title,
                'text': news.text,
                'created_at': news.created_at.strftime('%B %d, %Y, %I:%M %p'),
                'likes_count': news.likes.count(),
                'id': news.id,
            })
        return JsonResponse({'news': news_data})
    
    return render(request, 'news/news_list.html', {'page_obj': page_obj})

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
