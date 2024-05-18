# news/api_views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import News
from .serializers import NewsSerializer
from rest_framework import generics, permissions

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_news(request, pk=None):
    news = get_object_or_404(News, pk=pk)
    if request.user in news.likes.all():
        news.likes.remove(request.user)
    else:
        news.likes.add(request.user)
    return Response({'likes': news.likes.count()})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dislike_news(request, pk=None):
    news = get_object_or_404(News, pk=pk)
    if request.user in news.likes.all():
        news.likes.remove(request.user)
    return Response({'likes': news.likes.count()})


class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class NewsRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]