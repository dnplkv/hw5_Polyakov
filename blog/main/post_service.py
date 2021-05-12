from django.core.cache import cache

from .models import Post


def post_all():
    key = Post().__class__.cache_key()
    if key in cache:
        all_obj = cache.get(key)
    else:
        all_obj = Post.objects.all()
        cache.set(key, all_obj, 5)
    return all_obj


def post_find(post_id: int) -> Post:
    return Post.objects.get(id=post_id)
