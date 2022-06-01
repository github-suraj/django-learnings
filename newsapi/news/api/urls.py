from django.urls import path
from news.api.views import article_list, article_detail

urlpatterns = [
    path('articles/', article_list, name='article-list'),
    path('articles/<int:pk>/', article_detail, name='article-detail'),
]