from api.generics import AuthorSerializer, BooksSerializer, PostSerializer
from main.models import Author, Books, Post
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10


class BooksAPIViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('-id')
    serializer_class = BooksSerializer
    pagination_class = PageNumberPagination


class AuthorsAPIViewSet(generics.GenericAPIView):
    queryset = Author.objects.all().order_by('-id')

    def get(self, request):
        res = Author.objects.all().order_by('-id')
        ser = AuthorSerializer(res, many=True)
        return Response(ser.data)
