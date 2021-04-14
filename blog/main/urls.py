from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('about/', views.about, name='about'),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/imgs/favicon/favicon.ico')),

    path('posts/', views.posts, name='posts_all'),
    path('posts/create/', views.posts_create, name='posts_create'),
    path('posts/update/<int:post_id>/', views.posts_update, name='posts_update'),
    path('posts/<int:post_id>/', views.posts_show, name='posts_show'),

    path('authors/subscribe/', views.subscribers_new, name='subscribers_new'),
    path('subscribers/all/', views.subscribers_all, name='subscribers_all'),
    path('authors/new/', views.authors_new, name='authors_new'),
    path('authors/all/', views.authors_all, name='authors_all'),

    path('email_subs/', views.email_to_all_subs, name='email_to_all_subs'),

    path('api/posts/', views.json_posts, name='json_data'),
    path('api/subscribe/', views.api_subscribe, name='api_subscribe'),
    path('api/authors/new/', views.api_authors_new, name='api_authors_new'),
    path('api/subscribers/all/', views.api_subscribers_all, name='api_subscribers_all'),
    path('api/authors/all/', views.api_authors_all, name='api_authors_all'),
    path('api/posts/<int:post_id>/', views.api_posts_show, name='api_posts_show'),
]
