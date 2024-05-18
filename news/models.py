from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    tags = models.ManyToManyField(Tag, related_name='news')
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    views_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='liked_news', blank=True)

    def __str__(self):
        return self.title
