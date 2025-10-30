from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions
from django.db.models import F

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
        instance = self.get_object()

        # Atomic increment (preventing race conditions)
        Post.objects.filter(pk=instance.pk).update(views = F('views') + 1)
        instance.refresh_from_db() # Get updated value

        serializer = self.get_serializer(instance)

        return Response(serializer.data)
    