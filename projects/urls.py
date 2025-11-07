from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name='projects'),
    path('projects/create/', views.ProjectCreate.as_view(), name="project-create"),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name="project-update")
]
