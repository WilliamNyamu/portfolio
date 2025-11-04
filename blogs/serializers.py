from rest_framework import serializers
from .models import Post, Rating

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'excerpt', 'content', 'author', 'created_at', 'updated_at', 'views']
        read_only_fields = ['created_at', 'updated_at', 'author', 'views']

class RatingSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Rating
        fields = ['id', 'post', 'rating', 'overall']
        read_only_fields = ['overall']

    def validate(self, attrs):
        rating = attrs.get('rating')
        if rating < 0 or rating > 5:
            raise serializers.ValidationError("Rating is between 1 and 5")
        return attrs

    
    def create(self, validated_data):
        post = validated_data.get('post')
        rating = Rating.objects.filter(post=post).values_list('rating', flat=True)
        if rating:
            overall = sum(rating) / len(rating)
        else:
            overall = validated_data['rating']
        
        validated_data['rating'] = overall
        return super().create(validated_data)
    

