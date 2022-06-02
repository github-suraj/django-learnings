from django.urls import path
# from news.api.views import article_list, article_detail
from news.api.views import ArticleList, ArticleDetail, JournalistList

urlpatterns = [
    # path('articles/', article_list, name='article-list'),
    # path('articles/<int:pk>/', article_detail, name='article-detail'),
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('journalists/', JournalistList.as_view(), name='journalist-list'),
]