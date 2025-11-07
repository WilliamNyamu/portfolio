from django.shortcuts import render
from .serializers import ProjectSerializer
from .models import Project
from rest_framework import generics
from rest_framework import permissions

# Create your views here.
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    ordering = ['-created_at']

class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        message = "Project created successfully"
        context['message'] = message
        return context

class ProjectUpdate(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        message = "Project created successfully"
        context['message'] = message
        return context
    