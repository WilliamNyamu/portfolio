from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name="posts"),
    path('posts/<slug:slug>/', views.PostRetrieveView.as_view(), name="post-detail")
]