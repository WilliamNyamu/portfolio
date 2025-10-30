from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'excerpt', 'content', 'author', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'author']
    
    

