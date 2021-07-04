import django_filters
from main.models import Books, Post


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title']


class BooksFilter(django_filters.FilterSet):
    class Meta:
        model = Books
        fields = ['title']
