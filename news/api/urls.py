from django.urls import path
# from news.api.views import (article_list_create_api_view, article_detail_api_view)
from news.api.views import ( ArticleListCreateAPIView, ArticleDetailAPIView, JournalistListCreateAPIView)

urlpatterns = [
    # path('article/', article_list_create_api_view, name='article-list'),
    # path('article/<int:pk>', article_detail_api_view, name='article-detail'),
    path('article/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('article/<int:pk>', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('journalist/', JournalistListCreateAPIView.as_view(), name='journalist-list'),
]
