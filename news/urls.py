
from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('tag/<str:tag_name>/', views.news_by_tag, name='news_by_tag'),
    path('statistics/', views.news_statistics, name='news_statistics'),
    path('api/news/', api_views.NewsListCreateAPIView.as_view(), name='api_news_list_create'),
    path('api/news/<int:pk>/', api_views.NewsRetrieveDestroyAPIView.as_view(), name='api_news_detail_destroy'),
    path('api/news/<int:pk>/like/', api_views.like_news, name='like_news'),
    path('api/news/<int:pk>/dislike/', api_views.dislike_news, name='dislike_news'),
]
