from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions
from django.db.models import F
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


    def retrieve(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        instance = Post.objects.get(slug=slug)

        # Atomic increment (preventing race conditions)
        Post.objects.filter(slug=slug).update(views=F('views') + 1)
        instance.refresh_from_db()  # Get updated value

        serializer = self.get_serializer(instance)

        return Response(serializer.data)
    
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    

class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset
    
    def update(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        post = Post.objects.get(slug=slug)
        if post.author != request.user:
            return Response(
                {
                    'error': 'You do not have permission to edit this post.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        
        return super().update(request, *args, **kwargs)

    
class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = 'slug'
    