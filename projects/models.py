from django.db import models

# Create your models here.
"""
A projects has a name, excerpt, description, github_link, demo_link, photos, tech_stack
"""

class Project(models.Model):
    name=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=250)
    description=models.TextField()
    github_link=models.URLField()
    demo_link=models.URLField(blank=True, null=True)
    is_production=models.BooleanField(default=True)
    images=models.ImageField(upload_to="project_photos/")
    
    def __str__(self):
        return self.name
