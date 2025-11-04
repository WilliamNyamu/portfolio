from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=150, unique=True)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(blank=True, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Rating(models.Model):
    post=models.ForeignKey(Post, related_name="ratings", on_delete=models.CASCADE)
    rating=models.IntegerField()
    overall=models.FloatField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        ratings = Rating.objects.filter(post=self.post).values_list('rating', flat=True)
        overall = sum(ratings) / len(ratings)
        Rating.objects.filter(post=self.post).update(overall=overall)

    def __str__(self):
        return f'Rating {self.rating} for {self.post.title}'
    