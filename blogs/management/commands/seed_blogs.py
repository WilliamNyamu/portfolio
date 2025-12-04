from django.core.management import BaseCommand
from blogs.models import Post
from faker import Faker
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Seeding the Post Model with fake data"

    # Title, Slug, Excerpt, Content, author, created_at, updated_at, views
    def handle(self, *args, **kwargs):
        import random

        fake =Faker()
        self.stdout.write("Starting seeding")
        for i in range(10):
            Post.objects.create(
                title = fake.paragraph(),
                excerpt = fake.paragraph(),
                content = fake.paragraphs(),
                author = random.choice(User.objects.all()),
                views = random.randint(0, 100)
            )
            self.stdout.write(f"Seeding row {i+1} out of 10...")
        
        self.stdout.write("Finished seeding data")
