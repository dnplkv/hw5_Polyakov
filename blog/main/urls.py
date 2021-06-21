from blog import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.decorators import cache
from django.views.generic import TemplateView
# from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register(prefix='api/v1/posts_view', viewset=views.PostAPIViewSet, basename='post')

urlpatterns = [
    # path('', views.index, name='home_page'),
    path('', TemplateView.as_view(template_name='main/index.html'), name='home_page'),
    path('about/', views.about, name='about'),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/imgs/favicon/favicon.ico')),

    path('posts/', views.posts, name='posts_all'),
    path('posts/list/', views.PostsListView.as_view(), name='posts_list'),
    # path('posts/all/', cache.cache_page(30)(views.PostsListView.as_view()), name='posts_list'),
    path('posts/list/xlsx', views.DownloadPostsTitleXLSX.as_view(), name='download_posts_xlsx'),
    path('posts/create/', views.posts_create, name='posts_create'),
    path('posts/update/<int:post_id>/', views.posts_update, name='posts_update'),
    path('posts/<int:post_id>/', views.posts_show, name='posts_show'),

    path('authors/subscribe/', views.subscribers_new, name='subscribers_new'),
    path('subscribers/all/', views.subscribers_all, name='subscribers_all'),
    path('authors/new/', views.authors_new, name='authors_new'),
    # path('authors/all/', views.authors_all, name='authors_all'),
    path('authors/all/', cache.cache_page(30)(views.authors_all), name='authors_all'),
    path('books/all/', views.books_all, name='books_all'),
    path('books/list/', views.BooksListView.as_view(), name='books_list'),
    # path('categories/all/', views.categories_all, name='categories_all'),
    path('categories/all/', cache.cache_page(30)(views.categories_all), name='categories_all'),

    path('email_subs/', views.email_to_all_subs, name='email_to_all_subs'),

    path('posts/delete/<int:post_id>/', views.posts_delete, name='delete_posts'),
    path('authors/delete/<int:author_id>/', views.author_delete, name='delete_author'),

    path('api/v1/posts/', views.json_posts, name='json_data'),
    path('api/v1/posts/<int:post_id>/', views.api_posts_show, name='api_posts_show'),
    path('api/v1/subscribe/', views.api_subscribe, name='api_subscribe'),
    path('api/v1/authors/new/', views.api_authors_new, name='api_authors_new'),
    path('api/v1/subscribers/all/', views.api_subscribers_all, name='api_subscribers_all'),
    path('api/v1/authors/all/', views.api_authors_all, name='api_authors_all'),

    # API
    # path('api/v1/posts_view/', views.PostListAPIView.as_view(), name='api_posts'),
    # path('api/v1/posts_view/<int:post_id>/', views.PostAPIView.as_view(), name='api_posts_num'),
    path('api/v1/', include('api.urls')),

    path('contact-us/create/', views.ContactsView.as_view(), name='contact-us-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls
