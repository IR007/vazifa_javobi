from django.urls import path
from .views import (
    home_page_view,
    ArticleListView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    CommentCreateView,

)

urlpatterns = [
    path('', home_page_view, name='home'),
    path('articles/', ArticleListView.as_view(), name='blogs'),
    path('articles/article/new/', ArticleCreateView.as_view(), name='article_new'),
    path('articles/article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/article/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_new'),
]
