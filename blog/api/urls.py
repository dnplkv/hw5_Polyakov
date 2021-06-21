from rest_framework.routers import DefaultRouter

from .views import BooksAPIViewSet, PostAPIViewSet

api_name = 'api-test'

router = DefaultRouter()
router.register(prefix='posts_view', viewset=PostAPIViewSet, basename='post')
router.register(prefix='books_view', viewset=BooksAPIViewSet, basename='book')

urlpatterns = router.urls
