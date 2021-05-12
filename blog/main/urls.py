from django.urls import path
from django.views.decorators import cache
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # path('', views.index, name='home_page'),
    path('', TemplateView.as_view(template_name='main/index.html'), name='home_page'),
    path('about/', views.about, name='about'),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/imgs/favicon/favicon.ico')),

    path('posts/', views.posts, name='posts_all'),
    # path('posts/list/', views.PostsListView.as_view(), name='posts_list'),
    path('posts/all/', cache.cache_page(120)(views.PostsListView.as_view()), name='posts_list'),
    path('posts/list/xlsx', views.DownloadPostsTitleXLSX.as_view(), name='download_posts_xlsx'),
    path('posts/create/', views.posts_create, name='posts_create'),
    path('posts/update/<int:post_id>/', views.posts_update, name='posts_update'),
    path('posts/<int:post_id>/', views.posts_show, name='posts_show'),

    path('authors/subscribe/', views.subscribers_new, name='subscribers_new'),
    path('subscribers/all/', views.subscribers_all, name='subscribers_all'),
    path('authors/new/', views.authors_new, name='authors_new'),
    # path('authors/all/', views.authors_all, name='authors_all'),
    path('authors/all/', cache.cache_page(120)(views.authors_all), name='authors_all'),
    path('books/all/', views.books_all, name='books_all'),
    # path('categories/all/', views.categories_all, name='categories_all'),
    path('categories/all/', cache.cache_page(120)(views.categories_all), name='categories_all'),

    path('email_subs/', views.email_to_all_subs, name='email_to_all_subs'),

    path('api/posts/', views.json_posts, name='json_data'),
    path('api/subscribe/', views.api_subscribe, name='api_subscribe'),
    path('api/authors/new/', views.api_authors_new, name='api_authors_new'),
    path('api/subscribers/all/', views.api_subscribers_all, name='api_subscribers_all'),
    path('api/authors/all/', views.api_authors_all, name='api_authors_all'),
    path('api/posts/<int:post_id>/', views.api_posts_show, name='api_posts_show'),

    path('contact-us/create/', views.ContactsView.as_view(), name='contact-us-create'),
]
