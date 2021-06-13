from rest_framework.routers import DefaultRouter

from .views import PostAPIViewSet

api_name = 'api-test'

router = DefaultRouter()
router.register(prefix='posts_view', viewset=PostAPIViewSet, basename='post')

urlpatterns = router.urls
