from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['id', 'name', 'excerpt', 'description', 'github_link', 'demo_link', 'is_production', 'images']

    def validate(self, attrs):
        name = attrs.get('name')
        instance = self.instance # for update

        # If creating a new instance
        if not instance and Project.objects.filter(name=name).exists():
            raise serializers.ValidationError("The project name already exists")
        # If updating an existing instance
        if instance and Project.objects.filter(name=name).exclude(name=name).exists():
            raise serializers.ValidationError("During update, the name you're changing to is already taken")
    
        