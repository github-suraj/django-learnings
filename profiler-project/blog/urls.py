from django.urls import path
from .views import home, about, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', home, name='blog-home'),
    path('blogs/', PostListView.as_view(), name='blog-blogs'),
    path('blogs/<str:username>', UserPostListView.as_view(), name='user-blogs'),
    path('blogs/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('blogs/new/', PostCreateView.as_view(), name='blog-create'),
    path('blogs/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('blogs/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('about/', about, name='blog-about'),
]