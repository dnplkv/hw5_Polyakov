from main.models import Books, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'content',
            'created',
            'updated'
        )


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = (
            'id',
            'title',
            'author',
            'category',
        )
