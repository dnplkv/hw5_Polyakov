from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AuthorsAPIViewSet, BooksAPIViewSet, PostAPIViewSet

api_name = 'api-test'

router = DefaultRouter()
router.register(prefix='posts_view', viewset=PostAPIViewSet, basename='post')
router.register(prefix='books_view', viewset=BooksAPIViewSet, basename='book')
# router.register(prefix='authors_view', viewset=AuthorsAPIViewSet, basename='author')

urlpatterns = [
    path('authors/', AuthorsAPIViewSet.as_view(), name='authors')
]

urlpatterns.extend(router.urls)
