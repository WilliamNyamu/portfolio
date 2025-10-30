from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name="posts"),
    path('posts/<slug:slug>/', views.PostRetrieveView.as_view(), name="post-detail"),
    path('posts/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete')
]