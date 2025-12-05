from django.urls import path
from . import views
from .middleware import health_check

app_name = 'blog'

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile_detail'),
        path('post/new/', views.PostCreateView.as_view(), name='post_create'),
        path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
        path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
        path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]