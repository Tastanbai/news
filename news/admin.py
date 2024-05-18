# news/admin.py
from django.contrib import admin
from .models import News, Tag

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'views_count')
    search_fields = ('title', 'text')
    list_filter = ('tags', 'created_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
