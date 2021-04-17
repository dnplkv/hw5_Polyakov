import random

from django.core.management.base import BaseCommand
from faker import Faker
from main.models import Author
from main.models import Books
from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(75):
            Author(name=fake.name(), email=fake.email()).save()

        for _ in range(23):  # category name generator
            categories = ['Fantasy', 'Adventure', 'Romance', 'Contemporary',
                          'Dystopian', 'Mystery', 'Horror', 'Thriller', 'Paranormal',
                          'Historical fiction', 'Science Fiction', 'Memoir', 'Cooking',
                          'Art', 'Development', 'Motivational', 'Health', 'History',
                          'Travel', 'Guide', 'Social', 'Humor', 'Children’s']
            for _ in categories:
                value = random.choice(categories)
                if Category.objects.filter(name=value).exists() is False:
                    Category(name=value).save()
                else:
                    pass

        for _ in range(200):  # book title generator
            author = Author.objects.all().order_by('?').last()
            category = Category.objects.all().order_by('?').last()
            Books(title=fake.text(max_nb_chars=20).replace('.', ''), author=author, category=category).save()
