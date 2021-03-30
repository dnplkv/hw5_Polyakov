from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('posts/create', views.posts_create, name='posts_create'),
    path('api/posts', views.json_posts, name='json_data')
]
