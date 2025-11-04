from django.urls import path
from . import views

urlpatterns = [
    # Posting urlpatterns
    path('posts/', views.PostListView.as_view(), name="posts"),
    path('posts/<slug:slug>/', views.PostRetrieveView.as_view(), name="post-detail"),
    path('posts/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Rating urlpatterns
    path('ratings/<slug:slug>/', views.RatingView.as_view(), name='ratings'),
    path('ratings/<slug:slug>/create/', views.RatingCreateView.as_view(), name='rating-create'),
]